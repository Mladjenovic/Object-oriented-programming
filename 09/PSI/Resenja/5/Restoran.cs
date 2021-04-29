using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Z5
{
    class Restoran
    {
        private string naziv;
        private string adresa;
        private List<Stavka> jelovnik;   // za vezbu uraditi zadatak koriscenjem recnika

        #region props
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

        public string Adresa
        {
            get
            {
                return adresa;
            }

            set
            {
                adresa = value;
            }
        }

        #endregion

        public Restoran(string naziv, string adresa)
        {
            Naziv = naziv;
            Adresa = adresa;

            jelovnik = new List<Stavka>();
        }

        public void Import(string file)
        {
            StreamReader sr = null;
            string naziv;
            double cena;
            string linija;

            try
            {
                sr = new StreamReader(file);

                // petlja za kreiranje stavki (u fajlu je jedan red - jedna stavka)
                while ((linija = sr.ReadLine()) != null)
                {
                    //razdvajanje po delimiteru |
                    string[] lineParts = linija.Split('|');

                    naziv = lineParts[0];
                    cena = Double.Parse(lineParts[lineParts.Length - 2]); // ili lineParts[1], ovde dato kao primer kako da se pristupi nekom elementu sa kraja

                    if (! NazivStavkePostoji(naziv))
                        jelovnik.Add(new Stavka(naziv, cena));
                }
            }
            catch (Exception e) 
            {
                Console.WriteLine(e.Message);
                Console.WriteLine(e.StackTrace);
            }
            finally
            {
                if (sr != null){
                    sr.Close();
                }
            }
        }

        public void Sort()
        {
            Stavka tempI, tempJ;
            for (int i = 0; i < jelovnik.Count - 1; i++)
            {
                for (int j = i + 1; j < jelovnik.Count; j++)
                {
                    if (jelovnik[i].Cena < jelovnik[j].Cena)
                    {
                        tempI = jelovnik[i];
                        tempJ = jelovnik[j];
                        jelovnik.RemoveAt(j);
                        jelovnik.Insert(j, tempI);
                        jelovnik.RemoveAt(i);
                        jelovnik.Insert(i, tempJ);
                   }
                }
            }
        }

        public void Export(string file)
        {
            StreamWriter sw = null;

            try
            {
                sw = new StreamWriter(file);
                sw.WriteLine(this);
                sw.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.StackTrace);
            }
        }

        public override string ToString()
        {
            string str = "Restoran \"" + naziv + "\"\n"; // moze i Environment.NewLine
            str += "Adresa: " + adresa + "\n\n";
            if (jelovnik.Count == 0)
            {
                str += "Jelovnik je prazan";
            }
            else
            {
                str += "Jelovnik \n******************\n";
                foreach (Stavka s in jelovnik)
                    str += s + "\n";
                str += "******************\n";
            }
            return str;
        }

        // privatna pomocna metoda - nije obavezno
        private bool NazivStavkePostoji(string nazivStavke)
        {
            foreach (Stavka s in jelovnik)
            {
                if (s.Naziv == nazivStavke)
                {
                    return true;
                }
            }
            return false;
        }






    }
}
