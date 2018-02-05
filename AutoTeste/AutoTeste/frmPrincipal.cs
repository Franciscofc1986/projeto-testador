using AutoTeste.Comum;
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
    public partial class frmPrincipal : Form
    {
        Loading loadingBar = new Loading();

        public frmPrincipal()
        {
            exibirSplash();
            InitializeComponent();
        }

        private void exibirSplash()
        {
            Boolean result = true;
            loadingBar.Show();
            for (int i = 0; i <= 100; i++)
            {
                result = loadingBar.valor(i);
                if (result)
                {
                    System.Threading.Thread.Sleep(50);
                }
                else
                {
                    break;
                }
            }
            loadingBar.Close();
        }


        private void btnCriarTestes_Click(object sender, EventArgs e)
        {

        }
    }
}
