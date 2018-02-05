namespace AutoTeste.Comum
{
    partial class Loading
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
            this.pgressLoading = new System.Windows.Forms.ProgressBar();
            this.SuspendLayout();
            // 
            // pgressLoading
            // 
            this.pgressLoading.Location = new System.Drawing.Point(86, 65);
            this.pgressLoading.Name = "pgressLoading";
            this.pgressLoading.Size = new System.Drawing.Size(465, 23);
            this.pgressLoading.Step = 1;
            this.pgressLoading.TabIndex = 0;
            // 
            // Loading
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(676, 164);
            this.ControlBox = false;
            this.Controls.Add(this.pgressLoading);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.None;
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(676, 164);
            this.MinimizeBox = false;
            this.MinimumSize = new System.Drawing.Size(676, 164);
            this.Name = "Loading";
            this.ShowIcon = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Loading";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ProgressBar pgressLoading;
    }
}