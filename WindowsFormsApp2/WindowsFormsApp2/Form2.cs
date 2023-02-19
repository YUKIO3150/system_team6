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
    public partial class Form2 : Form
    {
        public Form2()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Program.text(Convert.ToString(textBox1.Text));
        }

        private void button2_Click(object sender, EventArgs e)
        {
            double a = Convert.ToDouble(comboBox2.Text);
            if (a < 0.5)
            {
                a = 0.5;
            }
            else if (a > 1.5)
            {
                a = 1.5;
            }
            Program.coeiroink(Convert.ToString(textBox1.Text),Convert.ToInt32(comboBox1.Text),a);
            Program.line();
        }
        private void button3_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
