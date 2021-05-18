package login_ragister_design;


import java.util.ArrayList;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;



/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Asus
 */
public class Http {
    private HttpClient httpClient;
    private HttpGet get;
    private HttpPost post;
    private HttpResponse response;
    private String resource;
    
    public Http(){
        this.httpClient = HttpClients.createDefault();
        this.get = null;
        this.resource = null;
    }
    
    public String GET(String URL){
        
        this.get = new HttpGet(URL);
        
        try{
            this.response = this.httpClient.execute(this.get);
            this.resource = EntityUtils.toString(this.response.getEntity());
        }catch(Exception e){
            System.out.println("ERROR: "+e);
        }
        
        return resource;
    }
    
    public String POST(String URL, String name, String password){
        
        this.post = new HttpPost(URL);
        
        try{
            //this.response = this.httpClient.execute(this.post);
            
            ArrayList<NameValuePair> postParameters;
            
            postParameters = new ArrayList<NameValuePair>();
            postParameters.add(new BasicNameValuePair("name", name));
            postParameters.add(new BasicNameValuePair("password", password));
            
            post.setEntity(new UrlEncodedFormEntity(postParameters, "UTF-8"));
            //httpclient = new DefaultHttpClient();

            //HttpResponse response = httpclient.execute(post);
            
            this.response = this.httpClient.execute(this.post);
            
            this.resource = EntityUtils.toString(this.response.getEntity());
        }catch(Exception e){
            System.out.println("ERROR: "+e);
        }
        
        return resource;
    }
}
