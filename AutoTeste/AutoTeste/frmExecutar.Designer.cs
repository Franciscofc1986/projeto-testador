namespace AutoTeste
{
    partial class frmExecutar
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.trvTestes = new System.Windows.Forms.TreeView();
            this.lblTestes = new System.Windows.Forms.Label();
            this.btnExecutarTestes = new System.Windows.Forms.Button();
            this.btnMarcarTodos = new System.Windows.Forms.Button();
            this.btnDownloadTests = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.lblTitulo = new System.Windows.Forms.Label();
            this.button4 = new System.Windows.Forms.Button();
            this.btnDesmarcarTodos = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // trvTestes
            // 
            this.trvTestes.CheckBoxes = true;
            this.trvTestes.Location = new System.Drawing.Point(12, 59);
            this.trvTestes.Name = "trvTestes";
            this.trvTestes.Size = new System.Drawing.Size(448, 382);
            this.trvTestes.TabIndex = 0;
            this.trvTestes.AfterCheck += new System.Windows.Forms.TreeViewEventHandler(this.trvTestes_AfterCheck);
            // 
            // lblTestes
            // 
            this.lblTestes.AutoSize = true;
            this.lblTestes.Location = new System.Drawing.Point(13, 44);
            this.lblTestes.Name = "lblTestes";
            this.lblTestes.Size = new System.Drawing.Size(85, 13);
            this.lblTestes.TabIndex = 3;
            this.lblTestes.Text = "Lista de Testes: ";
            // 
            // btnExecutarTestes
            // 
            this.btnExecutarTestes.Location = new System.Drawing.Point(12, 471);
            this.btnExecutarTestes.Name = "btnExecutarTestes";
            this.btnExecutarTestes.Size = new System.Drawing.Size(367, 35);
            this.btnExecutarTestes.TabIndex = 4;
            this.btnExecutarTestes.Text = "Executar os testes marcados";
            this.btnExecutarTestes.UseVisualStyleBackColor = true;
            this.btnExecutarTestes.Click += new System.EventHandler(this.btnExecutarTestes_Click);
            // 
            // btnMarcarTodos
            // 
            this.btnMarcarTodos.Location = new System.Drawing.Point(12, 442);
            this.btnMarcarTodos.Name = "btnMarcarTodos";
            this.btnMarcarTodos.Size = new System.Drawing.Size(94, 23);
            this.btnMarcarTodos.TabIndex = 5;
            this.btnMarcarTodos.Text = "Marcar todos";
            this.btnMarcarTodos.UseVisualStyleBackColor = true;
            this.btnMarcarTodos.Click += new System.EventHandler(this.btnMarcarTodos_Click);
            // 
            // btnDownloadTests
            // 
            this.btnDownloadTests.Location = new System.Drawing.Point(357, 442);
            this.btnDownloadTests.Name = "btnDownloadTests";
            this.btnDownloadTests.Size = new System.Drawing.Size(103, 23);
            this.btnDownloadTests.TabIndex = 6;
            this.btnDownloadTests.Text = "Baixar Testes";
            this.btnDownloadTests.UseVisualStyleBackColor = true;
            this.btnDownloadTests.Click += new System.EventHandler(this.btnDownloadTests_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(13, 15);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(43, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "Projeto:";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // lblTitulo
            // 
            this.lblTitulo.AutoSize = true;
            this.lblTitulo.Font = new System.Drawing.Font("Microsoft Sans Serif", 15.75F, ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline))), System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblTitulo.Location = new System.Drawing.Point(62, 6);
            this.lblTitulo.Name = "lblTitulo";
            this.lblTitulo.Size = new System.Drawing.Size(398, 25);
            this.lblTitulo.TabIndex = 7;
            this.lblTitulo.Text = "(Selecione um projeto na tela inicial)";
            // 
            // button4
            // 
            this.button4.Location = new System.Drawing.Point(385, 483);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(75, 23);
            this.button4.TabIndex = 8;
            this.button4.Text = "Voltar";
            this.button4.UseVisualStyleBackColor = true;
            this.button4.Click += new System.EventHandler(this.button4_Click);
            // 
            // btnDesmarcarTodos
            // 
            this.btnDesmarcarTodos.Location = new System.Drawing.Point(112, 442);
            this.btnDesmarcarTodos.Name = "btnDesmarcarTodos";
            this.btnDesmarcarTodos.Size = new System.Drawing.Size(111, 23);
            this.btnDesmarcarTodos.TabIndex = 9;
            this.btnDesmarcarTodos.Text = "Desmarcar todos";
            this.btnDesmarcarTodos.UseVisualStyleBackColor = true;
            this.btnDesmarcarTodos.Click += new System.EventHandler(this.btnDesmarcarTodos_Click);
            // 
            // frmExecutar
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(472, 514);
            this.Controls.Add(this.btnDesmarcarTodos);
            this.Controls.Add(this.button4);
            this.Controls.Add(this.lblTitulo);
            this.Controls.Add(this.btnDownloadTests);
            this.Controls.Add(this.btnMarcarTodos);
            this.Controls.Add(this.btnExecutarTestes);
            this.Controls.Add(this.lblTestes);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.trvTestes);
            this.Name = "frmExecutar";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Executar Testes";
            this.Shown += new System.EventHandler(this.frmExecutar_Shown);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.TreeView trvTestes;
        private System.Windows.Forms.Label lblTestes;
        private System.Windows.Forms.Button btnExecutarTestes;
        private System.Windows.Forms.Button btnMarcarTodos;
        private System.Windows.Forms.Button btnDownloadTests;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label lblTitulo;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Button btnDesmarcarTodos;
    }
}