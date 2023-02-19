using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WindowsFormsApp2
{
    public partial class Form4 : Form
    {
        public Form4()
        {
            InitializeComponent();
        }


        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            int d = 0;
            if (radioButton1.Checked == true) { d = 1; }
            Program.DBadd(Convert.ToString(textBox1.Text),1,Convert.ToInt32(comboBox1.Text),Convert.ToDouble(comboBox2.Text),d);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int d=0;
            if (radioButton1.Checked == true) { d = 1; }
            Program.DBadd(Convert.ToString(textBox1.Text), 2, Convert.ToInt32(comboBox1.Text), Convert.ToDouble(comboBox2.Text),d);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            int d=0;
            if (radioButton1.Checked == true) { d = 1; }
            Program.DBadd(Convert.ToString(textBox1.Text), 3, Convert.ToInt32(comboBox1.Text), Convert.ToDouble(comboBox2.Text),d);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int d=0;
            if (radioButton1.Checked == true) { d = 1; }
            Program.DBadd(Convert.ToString(textBox1.Text), 4, Convert.ToInt32(comboBox1.Text), Convert.ToDouble(comboBox2.Text),d);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int d=0;
            if (radioButton1.Checked == true) { d = 1; }
            Program.DBadd(Convert.ToString(textBox1.Text), 5, Convert.ToInt32(comboBox1.Text), Convert.ToDouble(comboBox2.Text),d);
        }
    }
}
