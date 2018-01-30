namespace AutoTeste
{
    partial class frmPrincipal
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
            this.cmbProjetos = new System.Windows.Forms.ComboBox();
            this.label1 = new System.Windows.Forms.Label();
            this.arvTestes = new System.Windows.Forms.TreeView();
            this.lblTestesProjeto = new System.Windows.Forms.Label();
            this.lblUsuario = new System.Windows.Forms.Label();
            this.btnExecutar = new System.Windows.Forms.Button();
            this.btnCriar = new System.Windows.Forms.Button();
            this.btnTrocarUsuario = new System.Windows.Forms.Button();
            this.btnCarregarProjeto = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // cmbProjetos
            // 
            this.cmbProjetos.FormattingEnabled = true;
            this.cmbProjetos.Location = new System.Drawing.Point(66, 36);
            this.cmbProjetos.Margin = new System.Windows.Forms.Padding(2);
            this.cmbProjetos.Name = "cmbProjetos";
            this.cmbProjetos.Size = new System.Drawing.Size(246, 21);
            this.cmbProjetos.TabIndex = 0;
            this.cmbProjetos.SelectedIndexChanged += new System.EventHandler(this.cmbProjetos_SelectedIndexChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(14, 39);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(48, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Projetos:";
            // 
            // arvTestes
            // 
            this.arvTestes.Location = new System.Drawing.Point(11, 128);
            this.arvTestes.Margin = new System.Windows.Forms.Padding(2);
            this.arvTestes.Name = "arvTestes";
            this.arvTestes.Size = new System.Drawing.Size(297, 327);
            this.arvTestes.TabIndex = 2;
            // 
            // lblTestesProjeto
            // 
            this.lblTestesProjeto.AutoSize = true;
            this.lblTestesProjeto.Location = new System.Drawing.Point(9, 113);
            this.lblTestesProjeto.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblTestesProjeto.Name = "lblTestesProjeto";
            this.lblTestesProjeto.Size = new System.Drawing.Size(90, 13);
            this.lblTestesProjeto.TabIndex = 3;
            this.lblTestesProjeto.Text = "Testes do Projeto";
            // 
            // lblUsuario
            // 
            this.lblUsuario.AutoSize = true;
            this.lblUsuario.Font = new System.Drawing.Font("Arial", 10.2F, System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblUsuario.Location = new System.Drawing.Point(9, 7);
            this.lblUsuario.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblUsuario.Name = "lblUsuario";
            this.lblUsuario.Size = new System.Drawing.Size(116, 16);
            this.lblUsuario.TabIndex = 5;
            this.lblUsuario.Text = "Nome do Usuário";
            // 
            // btnExecutar
            // 
            this.btnExecutar.Location = new System.Drawing.Point(190, 459);
            this.btnExecutar.Margin = new System.Windows.Forms.Padding(2);
            this.btnExecutar.Name = "btnExecutar";
            this.btnExecutar.Size = new System.Drawing.Size(118, 50);
            this.btnExecutar.TabIndex = 6;
            this.btnExecutar.Text = "Executar Testes";
            this.btnExecutar.UseVisualStyleBackColor = true;
            this.btnExecutar.Click += new System.EventHandler(this.btnExecutar_Click);
            // 
            // btnCriar
            // 
            this.btnCriar.Location = new System.Drawing.Point(11, 459);
            this.btnCriar.Margin = new System.Windows.Forms.Padding(2);
            this.btnCriar.Name = "btnCriar";
            this.btnCriar.Size = new System.Drawing.Size(118, 50);
            this.btnCriar.TabIndex = 7;
            this.btnCriar.Text = "Criar Testes";
            this.btnCriar.UseVisualStyleBackColor = true;
            this.btnCriar.Click += new System.EventHandler(this.btnCriar_Click);
            // 
            // btnTrocarUsuario
            // 
            this.btnTrocarUsuario.Location = new System.Drawing.Point(218, 2);
            this.btnTrocarUsuario.Name = "btnTrocarUsuario";
            this.btnTrocarUsuario.Size = new System.Drawing.Size(95, 22);
            this.btnTrocarUsuario.TabIndex = 8;
            this.btnTrocarUsuario.Text = "Trocar usuário";
            this.btnTrocarUsuario.UseVisualStyleBackColor = true;
            this.btnTrocarUsuario.Click += new System.EventHandler(this.btnTrocarUsuario_Click);
            // 
            // btnCarregarProjeto
            // 
            this.btnCarregarProjeto.Location = new System.Drawing.Point(107, 64);
            this.btnCarregarProjeto.Name = "btnCarregarProjeto";
            this.btnCarregarProjeto.Size = new System.Drawing.Size(117, 30);
            this.btnCarregarProjeto.TabIndex = 9;
            this.btnCarregarProjeto.Text = "Carregar Projeto";
            this.btnCarregarProjeto.UseVisualStyleBackColor = true;
            // 
            // frmPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(320, 516);
            this.Controls.Add(this.btnCarregarProjeto);
            this.Controls.Add(this.btnTrocarUsuario);
            this.Controls.Add(this.btnCriar);
            this.Controls.Add(this.btnExecutar);
            this.Controls.Add(this.lblUsuario);
            this.Controls.Add(this.lblTestesProjeto);
            this.Controls.Add(this.arvTestes);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.cmbProjetos);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "frmPrincipal";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Projeto Auto Teste";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.frmPrincipal_FormClosing);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.ComboBox cmbProjetos;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TreeView arvTestes;
        private System.Windows.Forms.Label lblTestesProjeto;
        private System.Windows.Forms.Label lblUsuario;
        private System.Windows.Forms.Button btnExecutar;
        private System.Windows.Forms.Button btnCriar;
        private System.Windows.Forms.Button btnTrocarUsuario;
        private System.Windows.Forms.Button btnCarregarProjeto;
    }
}