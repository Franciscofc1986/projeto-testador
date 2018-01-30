using AutoTeste.Model;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoTeste
{
    public partial class frmExecutar : Form
    {
        public List<Teste> lista_testes = new List<Teste>();

        public Configuracao configuracao = new Configuracao();



        public string Titulo = "";

        public frmExecutar()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void frmExecutar_Shown(object sender, EventArgs e)
        {
            if (lista_testes.Count > 0)
            {
                lblTitulo.Text = Titulo;
                lblTestes.Text = "Total de testes: " + lista_testes.Count();
                foreach (Teste teste in lista_testes)
                {
                    this.trvTestes.Nodes.Add(teste.key + " - (" + teste.fields.summary + ")");
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnExecutarTestes_Click(object sender, EventArgs e)
        {
            criarArquivoChamador();

            ProcessStartInfo pythonInfo = new ProcessStartInfo();
            Process python;
            pythonInfo.FileName = @"C:\Python36\python.exe";
            pythonInfo.Arguments = @"C:\\AutoTeste\\Executar_Testes.py";
            pythonInfo.CreateNoWindow = true;
            pythonInfo.UseShellExecute = false;
            // pythonInfo.WindowStyle = ProcessWindowStyle.Maximized;

            Console.WriteLine("Python Starting");
            python = Process.Start(pythonInfo);

            python.WaitForExit();
            python.Close();
        }

        private void criarArquivoChamador()
        {
            
            if(File.Exists("C:\\AutoTeste\\Executar_Testes.py"))
            {
                File.Delete("C:\\AutoTeste\\Executar_Testes.py");
            }

            using (StreamWriter sw = new StreamWriter("C:\\AutoTeste\\Executar_Testes.py"))
            {
                sw.Write("from Funcao import * \r\n");


                foreach (TreeNode node in trvTestes.Nodes)
                {
                    string chave = node.Text.Split(' ')[0];
                    if (node.Checked)
                    {
                        string arquivo = "C:\\AutoTeste\\Testes\\" + chave + ".py";
                        if (File.Exists(arquivo))
                        {
                            sw.Write("from Testes import " + chave + "\r\n");
                        }

                    }

                }

                sw.Write("\r\nif __name__ == \"__main__\": \r\n");
                sw.Write("\tunittest.main()");
                
            }
        }

        private void btnDownloadTests_Click(object sender, EventArgs e)
        {
            remover_testes();
            baixar_todos_testeAsync();
        }

        private void remover_testes()
        {
            System.IO.DirectoryInfo di = new DirectoryInfo("C:\\AutoTeste\\Testes");

            foreach (FileInfo file in di.GetFiles())
            {
                file.Delete();
            }
        }

        private async Task baixar_todos_testeAsync()
        {
            foreach (Teste teste in lista_testes)
            {
                await baixar_testeAsync(teste.fields.attachment.First().content, teste.fields.attachment.First().filename);
            }
        }

        private async Task baixar_testeAsync(string url, string nome)
        {
            try
            {
                using (var client = new HttpClient())
                {
                    client.BaseAddress = new Uri(url);
                    client.Timeout = TimeSpan.FromMinutes(5);

                    HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "");
                    request.Headers.Authorization =
                    new AuthenticationHeaderValue(
                        "Basic",
                        Convert.ToBase64String(
                            System.Text.ASCIIEncoding.ASCII.GetBytes(
                                string.Format("{0}:{1}", configuracao.Usuario, configuracao.Senha))));

                    await client.SendAsync(request)
                        .ContinueWith(responseTask =>
                        {
                            HttpResponseMessage resposta = responseTask.Result;

                            if (resposta.ReasonPhrase == "200" || resposta.StatusCode == HttpStatusCode.OK)
                            {
                                var httpStream = resposta.Content.ReadAsStringAsync().Result;

                                string OutputDirectory = "C:\\AutoTeste\\Testes";

                                if (!Directory.Exists(OutputDirectory))
                                {
                                    Directory.CreateDirectory(OutputDirectory);
                                }

                                criar_arquivo(OutputDirectory + "\\" + nome, httpStream);
                            }
                            else
                            {
                                Application.Exit();
                            }

                        });
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error, try again!");
            }
        }

        private void criar_arquivo(string filePath, string httpStream)
        {
            using (StreamWriter sw = new StreamWriter(filePath))
            {
                sw.Write(httpStream);
            }
        }

        private void trvTestes_AfterCheck(object sender, TreeViewEventArgs e)
        {
            if (e.Node.Checked)
            {

            }
        }

        private void btnMarcarTodos_Click(object sender, EventArgs e)
        {
            foreach (TreeNode node in trvTestes.Nodes)
            {
                node.Checked = true;
            }
        }

        private void btnDesmarcarTodos_Click(object sender, EventArgs e)
        {
            foreach (TreeNode node in trvTestes.Nodes)
            {
                node.Checked = false;
            }
        }
    }
}
