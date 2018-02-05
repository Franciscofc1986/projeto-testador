using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace AutoTeste
{
    public class ControlePrincipal
    {

        public void iniciar()
        {
            Application.Run(new frmLogin());
            Application.Run(new frmPrincipal());
            
        }
    }
}
