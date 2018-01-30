using AutoTeste.Model;
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
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
    public partial class frmLogin : Form
    {
        public frmPrincipal frm_principal = new frmPrincipal();
        public Configuracao configuracoes = new Configuracao();
        public bool processando = false;

        public frmLogin()
        {
            CheckForIllegalCrossThreadCalls = false;
            InitializeComponent();
            frm_principal.Show();
            frm_principal.Visible = false;
        }

        private void btnLogar_Click(object sender, EventArgs e)
        {
            //ExibirMsg("Processando...");
            
            configuracoes.EnderecoJira = txtURLJira.Text.Trim();
            configuracoes.LocalTestes = "C:\\AutoTeste";
            configuracoes.Usuario = txtUsuario.Text.Trim();
            configuracoes.Senha = txtSenha.Text.Trim();
            
            logar_jira();
            processarJaAsync();
        }

        private void logar_jira()
        {
            
            HttpClient client = new HttpClient();
            try
            {
                client.BaseAddress = new Uri(configuracoes.EnderecoJira + "/rest/api/2/user?username=" + configuracoes.Usuario);

            
            client.Timeout = TimeSpan.FromMilliseconds(20000);
            client.DefaultRequestHeaders
                  .Accept
                  .Add(new MediaTypeWithQualityHeaderValue("application/json"));//ACCEPT header

            HttpRequestMessage request = new HttpRequestMessage(HttpMethod.Get, "");
            request.Headers.Authorization =
            new AuthenticationHeaderValue(
                "Basic",
                Convert.ToBase64String(
                    System.Text.ASCIIEncoding.ASCII.GetBytes(
                        string.Format("{0}:{1}", configuracoes.Usuario, configuracoes.Senha))));

            client.SendAsync(request)
                    .ContinueWith(responseTask =>
                    {
                        try
                        {
                            HttpResponseMessage resposta = responseTask.Result;

                            if (resposta.ReasonPhrase == "200" || resposta.StatusCode == HttpStatusCode.OK)
                            {
                                ExibirMsg("Logado com sucesso");
                                string json = resposta.Content.ReadAsStringAsync().Result;
                                Usuario usuarioJira = JsonConvert.DeserializeObject<Usuario>(json);

                                if (chkSalvarDados.Checked)
                                {
                                    salvar_dados();
                                }

                                abrir_formPrincipal();
                            }
                            else
                            {
                                if (resposta.StatusCode == HttpStatusCode.Unauthorized)
                                {
                                    ExibirMsg("Usuário ou senha incorreto/s.", true);
                                }
                                else if (resposta.StatusCode == HttpStatusCode.Forbidden)
                                {
                                    ExibirMsg("Acesso não autorizado.", true);
                                }
                                else
                                {
                                    ExibirMsg("Falha ao tentar logar.", true);
                                }
                                
                            }
                        }catch(Exception except)
                        {
                            ExibirMsg("Endereço do Jira inválido.", true);
                        }

                    });
            }
            catch (Exception ex)
            {
                ExibirMsg("Endereço do Jira inválido.", true);
            }

        }

        private void ExibirMsg(string texto, bool falha = false)
        {
            processando = false;
            if (falha)
            {
                txtMsg.ForeColor = Color.Red;
            }
            else
            {
                txtMsg.ForeColor = Color.Black;
            }

            txtMsg.Text = texto;
            txtMsg.Refresh();
        }

        private async Task processarJaAsync()
        {
            txtMsg.ForeColor = Color.Black;
            Processar();
        }

        private async Task Processar()
        {
            processando = true;
            int cont = 0;
            string textoProcessando = "";
            while (processando)
            {
                cont++;
                textoProcessando = "Processando";

                if (cont == 10000000)
                {
                    textoProcessando += ".";
                    txtMsg.Text = textoProcessando;
                    txtMsg.Refresh();
                }

                if (cont == 20000000)
                {
                    textoProcessando += "..";
                    txtMsg.Text = textoProcessando;
                    txtMsg.Refresh();
                }

                if (cont == 30000000)
                {
                    textoProcessando += "...";
                    txtMsg.Text = textoProcessando;
                    txtMsg.Refresh();
                }

                if (cont > 40000000)
                {
                    cont = 0;
                    textoProcessando = "Processando";
                    txtMsg.Text = textoProcessando;
                    txtMsg.Refresh();
                }


            }
        }

        private void salvar_dados()
        {
            string text = "{\"EnderecoJira\":\"" + configuracoes.EnderecoJira + "\"," +
                          "\"LocalTestes\":\"" + "C:\\AutoTeste" + "\"," +
                          "\"Usuario\":\"" + configuracoes.Usuario + "\"," +
                          "\"Senha\":\"" + configuracoes.Senha + "\"}";
            
            using (StreamWriter sw = new StreamWriter("config.json"))
            {
                sw.Write(text);
            }
        }

        private void abrir_formPrincipal()
        {
            frm_principal.configuracao = configuracoes;
            frm_principal.exibir_Nome("Bem vindo, " + configuracoes.Usuario);
            frm_principal.Visible = true;
            frm_principal.listar_projetos();

            this.Hide();

        }

        private void txtSenha_TextChanged(object sender, EventArgs e)
        {

        }

        private bool abrir_configuracao_salva()
        {

            string startupPath = System.IO.Directory.GetCurrentDirectory();

            if (!File.Exists(startupPath + "\\config.json"))
            {
                return false;
            }

            using (StreamReader r = new StreamReader("config.json"))
            {
                string json = r.ReadToEnd();
                Configuracao configuracao = JsonConvert.DeserializeObject<Configuracao>(json);

                if (configuracao.Usuario != "")
                {
                    configuracoes = configuracao;
                    return true;
                }
                else
                {
                    return false;
                }

            }
        }

        private void frmLogin_Shown(object sender, EventArgs e)
        {
            if (abrir_configuracao_salva())
            {
                txtURLJira.Text = configuracoes.EnderecoJira;
                txtUsuario.Text = configuracoes.Usuario;
                txtSenha.Text = configuracoes.Senha;

                abrir_formPrincipal();
            }
        }

    }
}
