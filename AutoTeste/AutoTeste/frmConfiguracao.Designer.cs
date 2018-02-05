namespace AutoTeste
{
    partial class frmConfiguracao
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
            this.lblURL = new System.Windows.Forms.Label();
            this.lblSalvarSenha = new System.Windows.Forms.Label();
            this.cbxSalvarSenha = new System.Windows.Forms.CheckBox();
            this.txtURLJira = new System.Windows.Forms.TextBox();
            this.btnSalvarConfig = new System.Windows.Forms.Button();
            this.lblGit = new System.Windows.Forms.Label();
            this.txtGithub = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // lblURL
            // 
            this.lblURL.AutoSize = true;
            this.lblURL.Location = new System.Drawing.Point(113, 30);
            this.lblURL.Name = "lblURL";
            this.lblURL.Size = new System.Drawing.Size(66, 13);
            this.lblURL.TabIndex = 0;
            this.lblURL.Text = "URL do Jira:";
            // 
            // lblSalvarSenha
            // 
            this.lblSalvarSenha.AutoSize = true;
            this.lblSalvarSenha.Location = new System.Drawing.Point(14, 89);
            this.lblSalvarSenha.Name = "lblSalvarSenha";
            this.lblSalvarSenha.Size = new System.Drawing.Size(165, 13);
            this.lblSalvarSenha.TabIndex = 1;
            this.lblSalvarSenha.Text = "Salvar a senha automaticamente:";
            // 
            // cbxSalvarSenha
            // 
            this.cbxSalvarSenha.AutoSize = true;
            this.cbxSalvarSenha.Checked = true;
            this.cbxSalvarSenha.CheckState = System.Windows.Forms.CheckState.Checked;
            this.cbxSalvarSenha.Location = new System.Drawing.Point(182, 89);
            this.cbxSalvarSenha.Name = "cbxSalvarSenha";
            this.cbxSalvarSenha.Size = new System.Drawing.Size(15, 14);
            this.cbxSalvarSenha.TabIndex = 2;
            this.cbxSalvarSenha.UseVisualStyleBackColor = true;
            // 
            // txtURLJira
            // 
            this.txtURLJira.Location = new System.Drawing.Point(182, 28);
            this.txtURLJira.Name = "txtURLJira";
            this.txtURLJira.Size = new System.Drawing.Size(329, 20);
            this.txtURLJira.TabIndex = 3;
            this.txtURLJira.Text = "http://localhost:8080";
            // 
            // btnSalvarConfig
            // 
            this.btnSalvarConfig.Location = new System.Drawing.Point(182, 109);
            this.btnSalvarConfig.Name = "btnSalvarConfig";
            this.btnSalvarConfig.Size = new System.Drawing.Size(75, 23);
            this.btnSalvarConfig.TabIndex = 4;
            this.btnSalvarConfig.Text = "Salvar";
            this.btnSalvarConfig.UseVisualStyleBackColor = true;
            this.btnSalvarConfig.Click += new System.EventHandler(this.btnSalvarConfig_Click);
            // 
            // lblGit
            // 
            this.lblGit.AutoSize = true;
            this.lblGit.Location = new System.Drawing.Point(10, 55);
            this.lblGit.Name = "lblGit";
            this.lblGit.Size = new System.Drawing.Size(169, 13);
            this.lblGit.TabIndex = 5;
            this.lblGit.Text = "Endereço do repositório do github:";
            // 
            // txtGithub
            // 
            this.txtGithub.Location = new System.Drawing.Point(182, 55);
            this.txtGithub.Name = "txtGithub";
            this.txtGithub.Size = new System.Drawing.Size(329, 20);
            this.txtGithub.TabIndex = 6;
            this.txtGithub.Text = "https://github.com/Franciscofc1986/projeto-testador.git";
            // 
            // frmConfiguracao
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(523, 149);
            this.Controls.Add(this.txtGithub);
            this.Controls.Add(this.lblGit);
            this.Controls.Add(this.btnSalvarConfig);
            this.Controls.Add(this.txtURLJira);
            this.Controls.Add(this.cbxSalvarSenha);
            this.Controls.Add(this.lblSalvarSenha);
            this.Controls.Add(this.lblURL);
            this.Name = "frmConfiguracao";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Configurações";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblURL;
        private System.Windows.Forms.Label lblSalvarSenha;
        private System.Windows.Forms.CheckBox cbxSalvarSenha;
        private System.Windows.Forms.TextBox txtURLJira;
        private System.Windows.Forms.Button btnSalvarConfig;
        private System.Windows.Forms.Label lblGit;
        private System.Windows.Forms.TextBox txtGithub;
    }
}