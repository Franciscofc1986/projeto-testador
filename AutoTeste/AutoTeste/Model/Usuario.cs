using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutoTeste.Model
{
    public class Usuario
    {
        public string self { get; set; }
        public string key { get; set; }
        public string name { get; set; }
        public string emailAddress { get; set; }
        public object avatarUrls { get; set; }
        public string displayName { get; set; }
        public string active { get; set; }
        public string timeZone { get; set; }
        public string locale { get; set; }
        public object groups { get; set; }
        public object applicationRoles { get; set; }
        public string expand { get; set; }
    }
}
