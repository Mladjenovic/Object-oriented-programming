using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Z4
{
    [Serializable] // atribut koji omogucava serijalizaciju objekta
    class Osoba
    {
        #region fields
        private string ime;
        private string prezime;
        #endregion fields

        #region props
        public string Ime
        {
            get { return ime; }
            set { ime = value; }
        }

        public string Prezime
        {
            get { return prezime; }
            set { prezime = value; }
        }
        #endregion

        #region ctors
        public Osoba(string ime, string prezime)
        {
            Ime = ime;
            Prezime = prezime;
        }
        #endregion


        #region methods
        public override String ToString()
        {
            return "Osoba [ime=" + Ime + ", prezime=" + Prezime + "]";
        }
        #endregion
    }
}
