using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoTeste.Comum
{
    public partial class Loading : Form
    {
        public Loading()
        {
            InitializeComponent();
            pgressLoading.Value = 0;
        }

        public Boolean valor(int quantidade)
        {
            if (quantidade <= 100)
            {
                pgressLoading.Value = quantidade;
                this.Opacity = 1 - ((double)quantidade * 0.01);
                pgressLoading.Refresh();
                return true;
            }
            else
            {
                return false;
            }
            
        }
    }
}
