using System;
using System.Diagnostics;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Text.Json;
using System.Text.Json.Serialization;

namespace WindowsFormsApp2
{
    static class Program
    {
        static public string PYTHONPATH = "C:\\Users\\user\\DIR\\Scripts\\python.exe";
        public class n
        {
            public string text { get; set; }
            public int a { get; set; }
            public double b { get; set; }
            public int c { get; set; }
            public n(string text,int a,double b,int c)
            {
                this.text = text;
                this.a = a;
                this.b = b;
                this.c = c;
            }
        }
        /// <summary>
        /// アプリケーションのメイン エントリ ポイントです。
        /// </summary>
        [STAThread]
        static private async void sleepAsync(int a)
        {
            await Task.Delay(a);
        }
            static void Main()
        {
            System.Diagnostics.ProcessStartInfo p = new System.Diagnostics.ProcessStartInfo();
            p.FileName = "C:\\COEIROINK-CPU-v.1.6.0\\COEIROINK-CPU-v.1.6.0\\COEIROINKonVOICEVOX.exe";
            p.WindowStyle = System.Diagnostics.ProcessWindowStyle.Minimized;
            System.Diagnostics.Process psi = System.Diagnostics.Process.Start(p);
            sleepAsync(1000);
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
        static public void coeiroink(string text,int a,double b)
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\coe_3.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp + " " +text+ " " +a+" "+b
                }
            };

            myProcess.Start();
            myProcess.WaitForExit();
            myProcess.Close();
        }
        static public void text(string text)
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\text.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp + " " + text
                }
            };

            myProcess.Start();
            myProcess.WaitForExit();
            myProcess.Close();
        }

        static public void line()
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\line.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp
                }
            };

            myProcess.Start();
            myProcess.WaitForExit();
            myProcess.Close();
        }
        static public string[] python()
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\test124.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp
                }
            };
            myProcess.Start();
            int n = 0;
            string[] hairetu = new string[100];
            StreamReader myStreamReader = myProcess.StandardOutput;
            while (myStreamReader.Peek() != -1)
            {
                string myString = myStreamReader.ReadLine();
                hairetu[n] = Convert.ToString(myString);
                n++;
            }
            myProcess.WaitForExit();
            myProcess.Close();
            return hairetu;
        }
        static public n CallDB()
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\CallDB.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp
                }
            };
            myProcess.Start();
            StreamReader myStreamReader = myProcess.StandardOutput;
            var n1=new n(Convert.ToString(myStreamReader.ReadLine()), Convert.ToInt32(myStreamReader.ReadLine()), Convert.ToDouble(myStreamReader.ReadLine()), Convert.ToInt32(myStreamReader.ReadLine()));
            n1.text = Convert.ToString(myStreamReader.ReadLine());
            n1.a = Convert.ToInt32(myStreamReader.ReadLine());
            n1.b = Convert.ToDouble(myStreamReader.ReadLine());
            n1.c = Convert.ToInt32(myStreamReader.ReadLine());
            return n1;
        }
        static public void DBadd(string text,int a,int b,double c,int d)
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\Desktop\\WindowsFormsApp2\\PythonScript\\DBadd.py";
            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo(PYTHONPATH)
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp + " " + text + " " + a + " " + b + " "+ c +" " +d
                }
            };

            myProcess.Start();
            myProcess.WaitForExit();
            myProcess.Close();
        }
    }
}
