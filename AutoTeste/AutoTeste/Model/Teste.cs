using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AutoTeste.Model
{
    public class Teste
    {
        public long id {get; set;}
        public string key {get; set;}
        public string self {get; set;}
        public Campos fields {get; set;}
    }

    public class Campos
    {
        public string summary { get; set; }
        public List<Anexo> attachment { get; set; }
    }

    public class Anexo
    {
        public string id { get; set; }
        public string filename { get; set; }
        public string content { get; set; }
        public long size { get; set; }
    }
}
