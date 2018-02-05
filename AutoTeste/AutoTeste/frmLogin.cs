using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoTeste
{
    public partial class frmLogin : Form
    {
        frmConfiguracao frmConfig = new frmConfiguracao();
        frmSplashScreen frmSplash = new frmSplashScreen();

        public frmLogin()
        {
            InitializeComponent();
            exibirSplash();
            fecharSplash();
        }

        private void btnConfig_Click(object sender, EventArgs e)
        {
            frmConfig.Show();
        }

        public void exibirLogin(Form _frmPrincipal)
        {
            this.Show();
        }

        private void btnLogar_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void exibirSplash()
        {
            frmSplash.Show();
            System.Threading.Thread.Sleep(2000);

        }

        private void fecharSplash()
        {
            frmSplash.Close();
        }
    }
}
