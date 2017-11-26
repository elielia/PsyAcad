package bgu.psyacad.activities;

import android.content.Intent;
import android.content.SharedPreferences;
import android.content.res.AssetManager;
import android.graphics.Typeface;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ProgressBar;
import android.widget.TextView;

import com.google.gson.Gson;

import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.Queue;

import bgu.psyacad.R;
import bgu.psyacad.core.Word;
import bgu.psyacad.util.Constants;
import bgu.psyacad.util.GMailSender;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

public class EmailActivity extends AppCompatActivity {

    public static final String EMAIL_USERNAME = "eliashar@gmail.com";
    public static final String EMAIL_PASSWORD = "gunsguns12";
    SharedPreferences prefs=null;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);

        final ProgressBar bar=(ProgressBar) findViewById(R.id.progressBarEnter);


        Button button=(Button) findViewById(R.id.enter);
        final TextView mail=(TextView) findViewById(R.id.mailText);
        final TextView mailText=(TextView) findViewById(R.id.emailView);

        prefs=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());

        Typeface type2 = Typeface.createFromAsset(getBaseContext().getAssets(), "fonts/Alef-Regular.ttf");
        mailText.setTypeface(type2);

        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                bar.setVisibility(View.VISIBLE);

                ArrayList<Word> words = new ArrayList<Word>();

                ArrayList<Word> knownEnglish = new ArrayList<Word>();
                Queue<Word> mainQueueEnglish = new ArrayDeque<Word>();
                PriorityQueue<Word> seenQueueEnglish = new PriorityQueue<Word>();
                int numOfEnglishWords = 0;
                PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                ArrayList<Word> knownHebrew = new ArrayList<Word>();
                Queue<Word> mainQueueHebrew = new ArrayDeque<Word>();
                PriorityQueue<Word> seenQueueHebrew = new PriorityQueue<Word>();
                int numOfHebrewWords = 0;

                try {
                    AssetManager am = getAssets();
                    InputStream is = am.open("english.xls");
                    Workbook wb = Workbook.getWorkbook(is);
                    Sheet s= wb.getSheet(0);
                    numOfEnglishWords = s.getRows();
                    int id = 0;

                    for (int row=1; row<s.getRows(); row++){
                        Word englishWord = new Word(id, s.getCell(0,row).getContents(),s.getCell(1,row).getContents(),s.getCell(2,row).getContents());
                        words.add(englishWord);
                        id++;
                        mainQueueEnglish.add(englishWord);
                    }

                    is.close();
                    is = am.open("hebrew.xls");
                    wb = Workbook.getWorkbook(is);
                    s= wb.getSheet(0);
                    numOfHebrewWords = s.getRows();

                    for (int row=1; row<s.getRows(); row++){
                        Word hebrewWord = new Word(id, s.getCell(0,row).getContents(),s.getCell(1,row).getContents(),s.getCell(2,row).getContents());
                        words.add(hebrewWord);
                        id++;
                        mainQueueHebrew.add(hebrewWord);
                    }


                } catch (IOException e) {
                    finish();
                } catch (BiffException e) {
                    finish();
                }




                // Saving the data to files, after initializing

                Gson gson = new Gson();
                String words_string = gson.toJson(words);

                String known_english = gson.toJson(knownEnglish);
                String main_queue_english = gson.toJson(mainQueueEnglish);
                String seen_queue_english = gson.toJson(seenQueueEnglish);

                String known_hebrew = gson.toJson(knownHebrew);
                String main_queue_hebrew = gson.toJson(mainQueueHebrew);
                String seen_queue_hebrew = gson.toJson(seenQueueHebrew);


                SharedPreferences.Editor prefsEditor = prefs.edit();

                prefsEditor.putString(Constants.WORDS, words_string);
                prefsEditor.putString(Constants.KNOWN_ENGLISH, known_english);
                prefsEditor.putString(Constants.MAIN_QUEUE_ENGLISH, main_queue_english);
                prefsEditor.putString(Constants.SEEN_QUEUE_ENGLISH, seen_queue_english);
                prefsEditor.putString(Constants.KNOWN_HEBREW, known_hebrew);
                prefsEditor.putString(Constants.MAIN_QUEUE_HEBREW, main_queue_hebrew);
                prefsEditor.putString(Constants.SEEN_QUEUE_HEBREW, seen_queue_hebrew);
                prefsEditor.putInt(Constants.NUM_OF_ENGLISH_WORDS, numOfEnglishWords);
                prefsEditor.putInt(Constants.NUM_OF_HEBREW_WORDS,numOfHebrewWords);
                prefsEditor.putBoolean(Constants.IS_FIRST_TIME, false);

                prefsEditor.commit();


                new Thread(new Runnable() {
                    @Override
                    public void run() {
                        try {
                            GMailSender sender = new GMailSender(EMAIL_USERNAME, EMAIL_PASSWORD);
                            sender.sendMail(getResources().getString(R.string.subject_message),
                                    getResources().getString(R.string.body_message),
                                    "eliashar@gmail.com",
                                    mail.getText().toString());

                        } catch (Exception e) {
                            Log.e("SendMail", e.getMessage(), e);
                        }
                    }
                }).start();

                bar.setVisibility(View.INVISIBLE);

                Intent intent = new Intent(EmailActivity.this, MainActivity.class);
                startActivity(intent);
                finish();
            }
        });
    }


}
