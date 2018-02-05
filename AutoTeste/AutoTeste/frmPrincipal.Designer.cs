namespace AutoTeste
{
    partial class frmPrincipal
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">true se for necessário descartar os recursos gerenciados; caso contrário, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte ao Designer - não modifique 
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCriarTestes = new System.Windows.Forms.Button();
            this.btnExecutarTestes = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCriarTestes
            // 
            this.btnCriarTestes.Location = new System.Drawing.Point(100, 37);
            this.btnCriarTestes.Name = "btnCriarTestes";
            this.btnCriarTestes.Size = new System.Drawing.Size(130, 71);
            this.btnCriarTestes.TabIndex = 0;
            this.btnCriarTestes.Text = "Criar/Editar Testes";
            this.btnCriarTestes.UseVisualStyleBackColor = true;
            this.btnCriarTestes.Click += new System.EventHandler(this.btnCriarTestes_Click);
            // 
            // btnExecutarTestes
            // 
            this.btnExecutarTestes.Location = new System.Drawing.Point(100, 137);
            this.btnExecutarTestes.Name = "btnExecutarTestes";
            this.btnExecutarTestes.Size = new System.Drawing.Size(130, 76);
            this.btnExecutarTestes.TabIndex = 1;
            this.btnExecutarTestes.Text = "Executar Testes";
            this.btnExecutarTestes.UseVisualStyleBackColor = true;
            // 
            // frmPrincipal
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(325, 281);
            this.Controls.Add(this.btnExecutarTestes);
            this.Controls.Add(this.btnCriarTestes);
            this.Name = "frmPrincipal";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Software AutoTeste";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnCriarTestes;
        private System.Windows.Forms.Button btnExecutarTestes;
    }
}

