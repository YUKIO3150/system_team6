using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Python.Runtime;
using System.IO;

namespace WindowsFormsApp6
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //  モジュールのあるパスを追加
            //  exeのあるフォルダは、追加不要
            string[] pathes = {
                PythonEngine.PythonPath,
                Path.Combine(@"～")   //< Python Script ファイルのあるフォルダを設定
            };
            label1.Text = Convert.ToString(PythonEngine.PythonPath);
            //PythonEngine.PythonPath = string.Join(Path.PathSeparator.ToString(), pathes);
            //Console.WriteLine(PythonEngine.PythonPath);

            //PythonEngine.Initialize();

            //  Pythonのオブジェクト取得・操作前にロックが必要
            //IntPtr pythonLock = PythonEngine.AcquireLock();

            //  モジュールの実行と戻り値の取得
            //PyDict pyDict = new PyDict();
            //PythonEngine.Exec("import hogehoge", locals: pyDict.Handle);
            //var ret = PythonEngine.Eval("hogehoge.foo(58)", locals: pyDict.Handle);
            //Console.WriteLine(ret);

            //PythonEngine.ReleaseLock(pythonLock);

            //PythonEngine.Shutdown();
        }
    }
}
