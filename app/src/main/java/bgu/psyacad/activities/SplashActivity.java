package bgu.psyacad.activities;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.ProgressBar;

import bgu.psyacad.R;
import bgu.psyacad.util.Constants;

public class SplashActivity extends AppCompatActivity implements Runnable {


    SharedPreferences prefs=null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_splash);
        ProgressBar bar=(ProgressBar) findViewById(R.id.progressBar);
        bar.setVisibility(View.VISIBLE);

        prefs = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        Thread t=new Thread(this);
        t.start();

    }


    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
    }

    @Override
    public void run() {

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {

            if (prefs.getBoolean(Constants.IS_FIRST_TIME,true)) {

                Intent intent=new Intent(SplashActivity.this,EmailActivity.class);
                startActivity(intent);
                finish();

            } else{

                Intent intent=new Intent(SplashActivity.this,MainActivity.class);
                startActivity(intent);
                finish();
            }
        }
    }
}
