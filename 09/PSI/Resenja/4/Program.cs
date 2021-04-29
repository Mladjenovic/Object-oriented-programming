using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Runtime.Serialization.Formatters.Binary;
using System.IO;

namespace Z4
{
    /*
     * MonoDevelop: Options > TextEditor > CodeFolding > Enbale code folding
     * */
    class Program
    {
        static void Main(string[] args)
        {
            #region test save/load object

            Osoba o = new Osoba("Marko", "Markovic");
            string filePath = "Object.raw";  // moze i druga fajl ekstenzija  + ovo je relativna putanja (project > bin > Debug). Moze i apsolutna: "C:\\Object.raw"


            Console.WriteLine("Upis osobe u datoteku...");
            Snimi(filePath, o); 

            // pogledati da li vam se kreirao fajl
            // otvoriti u editoru, pogledati kako izgleda


            Console.WriteLine("Citanje osobe iz datoteke...");
            Osoba osoba = Ucitaj(filePath); 
            if (osoba != null)
                Console.WriteLine(osoba);  // da vidimo jel ucitavanje dobro urađeno

            #endregion


            Console.WriteLine("-------------------------------------");


            #region test save/load text

            // Tekst koji cemo snimati i učitavati može imati više redova
            int redovi = -1;
            while (redovi == -1)
            {
                Console.WriteLine("Koliko biste redova teksta da unesete u fajl?");

                try
                {
                    redovi = Int32.Parse(Console.ReadLine());
                }
                catch (Exception)
                {
                    Console.WriteLine("Niste uneli broj!");
                }
            }
            Console.WriteLine("Broj redova je: " + redovi);

            List<string> text = new List<string>();
            Console.WriteLine("Unesite zeljeni tekst:");

            for (int i = 0; i < redovi; i++)
                text.Add(Console.ReadLine());  


            string filePathText = "Text.txt";

            Console.WriteLine("Upis teksta u datoteku...");
            SnimiText(filePathText, text);

            // pogledati da li vam se kreirao fajl
            // otvoriti u editoru, pogledati kako izgleda

            Console.WriteLine("Citanje teksta iz datoteke...");
            List<string> textProcitan = UcitajText(filePathText); 

            for (int i = 0; i < textProcitan.Count; i++)
                Console.WriteLine(textProcitan[i]);

            #endregion test save/load text
        }

        #region metode za object

        public static void Snimi(string file, Osoba o)
        {
            BinaryFormatter bf = new BinaryFormatter(); // za serijalizaciju
            try
            {
                // F1 : Help
                FileStream fs = new FileStream(file, FileMode.Create, FileAccess.Write);  // path - relativna ili apsolutna putanja
                bf.Serialize(fs, o); // save

                fs.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine("Greška prilikom snimanja.");
                Console.WriteLine(e);
            }
        }

        public static Osoba Ucitaj(string file)
        {
            BinaryFormatter bf = new BinaryFormatter();
            Osoba osoba = null;
            
            if (File.Exists(file))
            {
                try
                {
                    FileStream fs = new FileStream(file, FileMode.Open, FileAccess.Read);
                    osoba = (Osoba)bf.Deserialize(fs); // ili osoba = bf.Deserialize(fs) as Osoba; //as vrаća null ako ne uspe; direct cast generiše izuzetak
                    fs.Close();
                }
                catch (Exception) // ako ne želimo da ispišemo detelje o grešci nije nam potreban objekat e
                {
                    Console.WriteLine("Greška prilikom čitanja");
                    
                }
            }

            return osoba; 
        }

        #endregion

        #region metode za text
        public static void SnimiText(string file, List<string> text)
        {
            StreamWriter sw = null;

            try
            {
                sw = new StreamWriter(file);
                for (int i = 0; i < text.Count; i++)
                {
                    sw.WriteLine(text[i]);
                }

                sw.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.StackTrace);
            }
        }

        public static List<string> UcitajText(string file)
        {
            StreamReader sr = null;
            string line;
            List<string> retVal = new List<string>();

            try
            {
                sr = new StreamReader(file);

                while ((line = sr.ReadLine()) != null)
                {
                    retVal.Add(line);
                }

                sr.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.StackTrace);
            }

            return retVal;
        }
        #endregion save/load text
    }
}
