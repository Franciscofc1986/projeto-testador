using AutoTeste.Model;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoTeste
{
    public partial class frmPrincipal : Form
    {
        public Configuracao configuracao = new Configuracao();

        List<Teste> lista_de_testes = new List<Teste>();

        public delegate void MyDelegate(List<Teste> lista);

        public delegate void MyDelegate2(Teste teste);

        public frmPrincipal()
        {
            InitializeComponent();
        }

        private void btnCriar_Click(object sender, EventArgs e)
        {

        }

        public void exibir_Nome(string nome_usuario)
        {
            lblUsuario.Text = nome_usuario;
        }

        public void listar_projetos()
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(configuracao.EnderecoJira + "/rest/api/2/project");
            client.DefaultRequestHeaders
                  .Accept
                  .Add(new MediaTypeWithQualityHeaderValue("application/json"));//ACCEPT header

            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "");
            request.Headers.Authorization =
            new AuthenticationHeaderValue(
                "Basic",
                Convert.ToBase64String(
                    System.Text.ASCIIEncoding.ASCII.GetBytes(
                        string.Format("{0}:{1}", configuracao.Usuario, configuracao.Senha))));

            client.SendAsync(request)
                  .ContinueWith(responseTask =>
                  {
                      HttpResponseMessage resposta = responseTask.Result;
                      string json = resposta.Content.ReadAsStringAsync().Result;
                      List<Projetos> lista_projetos = JsonConvert.DeserializeObject<List<Projetos>>(json);

                      foreach(Projetos item in lista_projetos)
                      {
                          cmbProjetos.Items.Add(item.key);
                      }
                  });
        }

        private void cmbProjetos_SelectedIndexChanged(object sender, EventArgs e)
        {
            arvTestes.Nodes.Clear();
            lista_de_testes.Clear();
            string itemSelecionado = (string)cmbProjetos.SelectedItem;
            buscarTestes(itemSelecionado);

            //arvTestes.Nodes.Clear();
            //string itemSelecionado = (string)cmbProjetos.SelectedItem;
            //string urlProjeto = configuracao.LocalTestes + itemSelecionado + "/";
            //if (Directory.Exists(urlProjeto))
            //{

            //    DirectoryInfo di = new DirectoryInfo(urlProjeto);
            //    FileInfo[] smFiles = di.GetFiles(itemSelecionado+"_Teste*");
            //    foreach (FileInfo fileName in smFiles)
            //        arvTestes.Nodes.Add(Path.GetFileNameWithoutExtension(fileName.Name));
            //}

        }

        private void buscarTestes(string Projeto)
        {
            HttpClient client = new HttpClient();
            client.BaseAddress = new Uri(configuracao.EnderecoJira + "/rest/raven/1.0/api/test?jql=project=" + Projeto);
            client.DefaultRequestHeaders
                  .Accept
                  .Add(new MediaTypeWithQualityHeaderValue("application/json"));//ACCEPT header

            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "");
            request.Headers.Authorization =
            new AuthenticationHeaderValue(
                "Basic",
                Convert.ToBase64String(
                    System.Text.ASCIIEncoding.ASCII.GetBytes(
                        string.Format("{0}:{1}", configuracao.Usuario, configuracao.Senha))));

            client.SendAsync(request)
                  .ContinueWith(responseTask =>
                  {
                      HttpResponseMessage resposta = responseTask.Result;
                      string json = resposta.Content.ReadAsStringAsync().Result;
                      List<Teste> lista_testes = new List<Teste>();
                      lista_testes = JsonConvert.DeserializeObject<List<Teste>>(json);
                      lblTestesProjeto.Text = "Total de testes: " + lista_testes.Count();
                      BeginInvoke(new MyDelegate(DelegateMethod), lista_testes);

                  });

        }

        public void DelegateMethod(List<Teste> lista)
        {
            foreach (Teste teste in lista)
            {
                conferir_teste(teste.self);
            }

        }

        public void DelegateMethod2(Teste teste)
        {

            if (teste.fields.attachment != null && teste.fields.attachment.Count > 0)
            {
                arvTestes.Nodes.Add(teste.key + " - (Automatizado)");
                lista_de_testes.Add(teste);
            }
            else
            {
                arvTestes.Nodes.Add(teste.key);
            }
        }

        private void conferir_teste(string url)
        {
            try
            {
                HttpClient client = new HttpClient();
                client.BaseAddress = new Uri(url);
                client.DefaultRequestHeaders
                      .Accept
                      .Add(new MediaTypeWithQualityHeaderValue("application/json"));//ACCEPT header

                HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "");
                request.Headers.Authorization =
                new AuthenticationHeaderValue(
                    "Basic",
                    Convert.ToBase64String(
                        System.Text.ASCIIEncoding.ASCII.GetBytes(
                            string.Format("{0}:{1}", configuracao.Usuario, configuracao.Senha))));

                client.SendAsync(request)
                      .ContinueWith(responseTask =>
                      {
                          HttpResponseMessage resposta = responseTask.Result;
                          string json = resposta.Content.ReadAsStringAsync().Result;
                          Teste teste = JsonConvert.DeserializeObject<Teste>(json);
                          BeginInvoke(new MyDelegate2(DelegateMethod2), teste);
                      });
            }
            catch
            {

            }
 
        }


        private void frmPrincipal_FormClosing(object sender, FormClosingEventArgs e)
        {
            Application.Exit();
        }

        private void btnTrocarUsuario_Click(object sender, EventArgs e)
        {
            string startupPath = System.IO.Directory.GetCurrentDirectory();

            File.Delete(startupPath + "\\config.json");

            Application.Restart();
        }

        private void run_cmd()
        {
            ProcessStartInfo pythonInfo = new ProcessStartInfo();
            Process python;
            pythonInfo.FileName = @"C:\Python36\python.exe";
            pythonInfo.Arguments = @"C:\Users\francisco_faria\AutoTeste\MQJ_Logar.py";
            pythonInfo.CreateNoWindow = true;
            pythonInfo.UseShellExecute = false;
            // pythonInfo.WindowStyle = ProcessWindowStyle.Maximized;

            Console.WriteLine("Python Starting");
            python = Process.Start(pythonInfo);
            
            python.WaitForExit();
            python.Close();         

        }

        private void btnExecutar_Click(object sender, EventArgs e)
        {
            frmExecutar form_Executar = new frmExecutar();
            form_Executar.lista_testes = lista_de_testes;
            form_Executar.configuracao = configuracao;
            form_Executar.Titulo = (string)cmbProjetos.SelectedItem;
            form_Executar.Show();
        }
    }


}
