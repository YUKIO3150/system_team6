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
    public partial class Form3 : Form
    {
        public Form3()
        {
            InitializeComponent();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string[] item = Program.python();
            comboBox1.Items.Clear();
            for (int i = 0; item[i] != null; i++)
            {
                comboBox1.Items.Add(item[i]);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double a = Convert.ToDouble(comboBox3.Text);
            if (a < 0.5)
            {
                a = 0.5;
            }
            else if (a > 1.5){
                a = 1.5;
            }
            Program.coeiroink(Convert.ToString(comboBox1.Text), Convert.ToInt32(comboBox2.Text),a);
        }
    }
}
