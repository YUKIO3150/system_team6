using System;
using System.Diagnostics;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    static class Program
    {
        /// <summary>
        /// アプリケーションのメイン エントリ ポイントです。
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new Form1());
        }
        static public void coeiroink(string text,int a)
        {
            //下記のPythonスクリプトへのファイルパスを記述する
            string myPythonApp = "C:\\Users\\user\\DIR\\coeiroink.py";

            var myProcess = new Process
            {
                StartInfo = new ProcessStartInfo("C:\\Users\\user\\DIR\\Scripts\\python.exe")
                {
                    UseShellExecute = false,
                    RedirectStandardOutput = true,
                    Arguments = myPythonApp + " " +text+ " " +a
                }
            };

            myProcess.Start();
            myProcess.WaitForExit();
            myProcess.Close();
        }
    }
}
