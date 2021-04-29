using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Z5
{
    class Stavka
    {
        private string naziv;
        private double cena;

        public string Naziv
        {
            get
            {
                return naziv;
            }

            set
            {
                naziv = value;
            }
        }

        public double Cena
        {
            get
            {
                return cena;
            }

            set
            {
                cena = value;
            }
        }

        public Stavka(string naziv, double cena)
        {
            Naziv = naziv;
            Cena = cena;
        }

        public override string ToString()
        {
            return Naziv + " " + Cena;
        }


    }
}
