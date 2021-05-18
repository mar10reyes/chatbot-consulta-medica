
package login_ragister_design;

import com.google.gson.Gson;
import com.google.gson.JsonParser;
import java.awt.Color;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JButton;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import org.json.*;

public class Main extends javax.swing.JFrame {

    String pregunta, respuesta,preguntagenerada;
    boolean reproducciendo=false;
     
     
    
    public Main() {
        initComponents();
    }

    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        enviar = new javax.swing.JButton();
        texto = new javax.swing.JTextField();
        jScrollPane1 = new javax.swing.JScrollPane();
        pantalla = new javax.swing.JTextArea();
        online = new javax.swing.JLabel();
        Namebot = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        enviar.setBackground(new java.awt.Color(255, 255, 255));
        enviar.setText("enviar");
        enviar.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        enviar.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                enviarActionPerformed(evt);
            }
        });

        texto.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                textoActionPerformed(evt);
            }
        });

        pantalla.setEditable(false);
        pantalla.setColumns(20);
        pantalla.setFont(new java.awt.Font("Lucida Sans Unicode", 0, 12)); // NOI18N
        pantalla.setRows(5);
        jScrollPane1.setViewportView(pantalla);

        online.setFont(new java.awt.Font("Tahoma", 0, 16)); // NOI18N

        Namebot.setFont(new java.awt.Font("Tahoma", 0, 17)); // NOI18N
        Namebot.setText("ChatBot");

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(texto)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.UNRELATED)
                        .addComponent(enviar))
                    .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 683, Short.MAX_VALUE)
                    .addGroup(layout.createSequentialGroup()
                        .addComponent(Namebot)
                        .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                        .addComponent(online, javax.swing.GroupLayout.PREFERRED_SIZE, 95, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(0, 0, Short.MAX_VALUE)))
                .addContainerGap())
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(online, javax.swing.GroupLayout.PREFERRED_SIZE, 21, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(Namebot))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jScrollPane1, javax.swing.GroupLayout.DEFAULT_SIZE, 193, Short.MAX_VALUE)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(enviar)
                    .addComponent(texto, javax.swing.GroupLayout.PREFERRED_SIZE, 23, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(19, 19, 19))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void enviarActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_enviarActionPerformed
        // TODO add your handling code here:

        String message = texto.getText();
        
        JSONObject response = new JSONObject(chatbotResponse(message));
        
        pantalla.append("Yo: "+message+
                "\nBot: "+response.getString("answer ")+"\n");
    }//GEN-LAST:event_enviarActionPerformed

   
    private void textoActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_textoActionPerformed


    }//GEN-LAST:event_textoActionPerformed

    public JButton enviarPresionado(){
        return enviar;
    }
    public void setPanatalla(){
        pantalla.append("Maquina: "+ respuesta+"\n");
    }
    public JTextArea regresaPantalla(){
        return pantalla;
    }
    

    public JTextField regresaTexto(){
        return texto;
    }
    
    public String chatbotResponse(String message)
    {
        Http peticion = new Http();
        return peticion.GET("https://chatbot-seminario.herokuapp.com/api/chatbot/?message="+message);
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel Namebot;
    private javax.swing.JButton enviar;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JLabel online;
    private javax.swing.JTextArea pantalla;
    private javax.swing.JTextField texto;
    // End of variables declaration//GEN-END:variables
}
