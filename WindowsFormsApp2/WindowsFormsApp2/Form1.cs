﻿using System;
using System.Diagnostics;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Imaging;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Runtime.InteropServices;
using Python.Runtime;

namespace WindowsFormsApp2
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// pythonライブラリを共有して使うための変数
        /// </summary>
        public class n
        {
            public string text { get; set; }
            public int a { get; set; }
            public double b { get; set; }
            public int c { get; set; }
            public n(string text, int a, double b, int c)
            {
                this.text = text;
                this.a = a;
                this.b = b;
                this.c = c;
            }
        }
        public Form1()
        {
            InitializeComponent();
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Form2 f2 = new Form2();
            f2.ShowDialog();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form3 f3 = new Form3();
            f3.ShowDialog();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Form4 f4 = new Form4();
            f4.ShowDialog();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            var n1=(n)Program.CallDB();
        }
    }
}