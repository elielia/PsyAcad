package bgu.psyacad.fragments;

import android.graphics.Typeface;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.lang.reflect.Field;
import java.util.ArrayList;
import java.util.Calendar;
import java.util.Date;
import java.util.PriorityQueue;
import java.util.concurrent.ArrayBlockingQueue;

import bgu.psyacad.R;
import bgu.psyacad.activities.MainActivity;
import bgu.psyacad.core.Word;
import bgu.psyacad.util.DataHolder;
import bgu.psyacad.util.PsyUtils;

/**
 * Created by ilayeliashar on 02/01/2016.
 */
public class EnglishFragment extends Fragment {
    private String[] wordsArrayString,transArrayString;
    private ArrayList<Word> words,know;
    private PriorityQueue<Word> seenQueue;
    private ArrayBlockingQueue<Word> mainQueue;
    private Button pullWordButton,againButton,goodButton,easyButton,knowButton, showAnswer;
    private ImageButton sound;
    private Word currentWord;
    private TextView currentWordView,currentWordTransView,currentWordDescView;
    private boolean takenFromMainQueue=true;
    private LinearLayout buttons,colors;
    private ImageView lineShowAnswer;
    private boolean showClicked=false;
    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view=inflater.inflate(R.layout.words_layout, container, false);


        initViews(view);
        initAnswerCover();

        if (currentWord==null) pullWord();
        else setText(currentWord);


        againButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (takenFromMainQueue) currentWord= DataHolder.mainQueueEnglish.poll();
                else currentWord=DataHolder.seenQueueEnglish.poll();
                calculateNewDateForWord(currentWord, 1);
                pullWord();

            }
        });

        goodButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (takenFromMainQueue) currentWord=DataHolder.mainQueueEnglish.poll();
                else currentWord=DataHolder.seenQueueEnglish.poll();
                calculateNewDateForWord(currentWord, 2);
                pullWord();

            }
        });

        easyButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (takenFromMainQueue) currentWord=DataHolder.mainQueueEnglish.poll();
                else currentWord=DataHolder.seenQueueEnglish.poll();
                calculateNewDateForWord(currentWord, 3);
                pullWord();

            }
        });

        knowButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                DataHolder.setWordIsKnown(currentWord.getId(), true);
                MainActivity.adapter.notifyDataSetChanged();
                if (takenFromMainQueue) currentWord=DataHolder.mainQueueEnglish.poll();
                else currentWord=DataHolder.seenQueueEnglish.poll();
                DataHolder.knownEnglish.add(currentWord);
                pullWord();

            }
        });


        showAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                showClicked=true;
                colors.setVisibility(View.VISIBLE);
                buttons.setVisibility(View.VISIBLE);
                currentWordTransView.setVisibility(View.VISIBLE);
                currentWordDescView.setVisibility(View.VISIBLE);
                showAnswer.setVisibility(View.INVISIBLE);
                lineShowAnswer.setVisibility(View.INVISIBLE);
            }
        });

        sound.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    if (currentWord != null) {
                        MediaPlayer mediaPlayer = MediaPlayer.create(getActivity().getApplicationContext(), getId("sound" + String.valueOf(currentWord.getId())));
                        if (mediaPlayer != null)
                            mediaPlayer.start(); // no need to call prepare(); create() does that for you
                    }
                } catch (RuntimeException e){
                    System.out.println("No sound for this word");
                }
            }
        });


        return view;
    }




    private void pullWord() {

        setVisibilityOfButtons();
        Date today= PsyUtils.getCurrentDate();
        Word wordFromMain=DataHolder.mainQueueEnglish.peek();
        Word wordFromSeen=DataHolder.seenQueueEnglish.peek();

        if (wordFromMain!=null && wordFromSeen!=null){


            currentWord=DataHolder.seenQueueEnglish.peek();
            if (today.before(currentWord.getNextDate())){
                currentWord=DataHolder.mainQueueEnglish.peek();
                takenFromMainQueue=true;
            }
            else {
                currentWord = DataHolder.seenQueueEnglish.peek();
                takenFromMainQueue=false;
            }
           setText(currentWord);


        }
        else if (wordFromMain!=null && wordFromSeen==null){
            currentWord=DataHolder.mainQueueEnglish.peek();
            takenFromMainQueue=true;
            setText(currentWord);
        }
        else if (wordFromMain==null && wordFromSeen!=null){
            currentWord=DataHolder.seenQueueEnglish.peek();
            takenFromMainQueue=false;
            if (!today.before(currentWord.getNextDate())){
                setText(currentWord);
            }
            else{
                currentWordView.setText("Oh Oh...It's too early for another word!");
                disableButtons();
            }
        }
        else if(wordFromMain==null && wordFromSeen==null){
            currentWordView.setText("Hurray! you finished the words...");
            disableButtons();
        }


    }

    private void disableButtons(){
        showAnswer.setEnabled(false);
        sound.setEnabled(false);
    }


    public double getNewEFactor(double oldEfactor,int qualityResponse) {
        double newEFactor = oldEfactor +(0.1-(5-qualityResponse)*(0.08+(5-qualityResponse)*0.02));
        if (newEFactor < 1.3) newEFactor = 1.3;
        return newEFactor;
    }

    private void setText (Word currentWord){
        currentWordView.setText(currentWord.getWord());
        currentWordTransView.setText(currentWord.getTranslation());
        currentWordDescView.setText(currentWord.getDescription());
    }


    public static int getId(String resourceName) {
        try {
            Field idField = (R.raw.class).getDeclaredField(resourceName);
            return idField.getInt(idField);
        } catch (Exception e) {
            throw new RuntimeException("No resource ID found for: "
                    + resourceName + " / " + (R.raw.class), e);
        }
    }

    private void calculateNewDateForWord(Word currentWord, int qualityResponse) {

        Calendar c=Calendar.getInstance();
        c.setTime(new Date());
        int n=currentWord.getTimesSeen();
        double eFactor=currentWord.getEF();

        if (n==1){
            currentWord.setDateBy(1);
        }
        else if(n==2){
            currentWord.setPreviousInterval(6);
            currentWord.setDateBy(6);
        }
        else if(n>2){
            int increaseDateby=(int)(currentWord.getPreviousInterval()*currentWord.getEF());
            currentWord.setPreviousInterval((int)increaseDateby);
            currentWord.setDateBy(increaseDateby);
        }
        currentWord.setEF(getNewEFactor(eFactor, qualityResponse));
        currentWord.increaseTimesSeen();
        DataHolder.seenQueueEnglish.add(currentWord);
    }

    private void initAnswerCover(){

        if(!showClicked){
            currentWordTransView.setVisibility(View.INVISIBLE);
            currentWordDescView.setVisibility(View.INVISIBLE);
            showAnswer.setVisibility(View.VISIBLE);
            lineShowAnswer.setVisibility(View.VISIBLE);
        }
        else{
            currentWordTransView.setVisibility(View.VISIBLE);
            currentWordDescView.setVisibility(View.VISIBLE);
            showAnswer.setVisibility(View.INVISIBLE);
            lineShowAnswer.setVisibility(View.INVISIBLE);
            colors.setVisibility(View.VISIBLE);
            buttons.setVisibility(View.VISIBLE);

        }
    }

    private void initViews(View view){

        againButton=(Button) view.findViewById(R.id.againButton);
        goodButton=(Button) view.findViewById(R.id.goodButton);
        easyButton=(Button) view.findViewById(R.id.easyButton);
        knowButton=(Button) view.findViewById(R.id.knowButton);
        showAnswer=(Button) view.findViewById(R.id.showAnswerButton);
        sound=(ImageButton) view.findViewById(R.id.soundButton);
        buttons=(LinearLayout) view.findViewById(R.id.layoutOfColorButtons);
        colors=(LinearLayout) view.findViewById(R.id.layoutOfLevel);
        lineShowAnswer=(ImageView) view.findViewById(R.id.line1);
        showAnswer.setHeight(againButton.getHeight()-lineShowAnswer.getHeight());
        currentWordView= (TextView) view.findViewById(R.id.currentWordView);
        currentWordTransView= (TextView) view.findViewById(R.id.currentWordTransView);
        currentWordDescView=(TextView) view.findViewById(R.id.currentWordDescView);
        Typeface type = Typeface.createFromAsset(getActivity().getAssets(), "fonts/Alef-Regular.ttf");
        Typeface type2 = Typeface.createFromAsset(getActivity().getAssets(),"fonts/NotoSansHebrew-Regular.ttf");
        currentWordTransView.setTypeface(type);
        currentWordView.setTypeface(type);
        currentWordDescView.setTypeface(type2);
    }

    private void setVisibilityOfButtons(){

        showClicked=false;
        colors.setVisibility(View.INVISIBLE);
        buttons.setVisibility(View.INVISIBLE);
        currentWordTransView.setVisibility(View.INVISIBLE);
        currentWordDescView.setVisibility(View.INVISIBLE);
        showAnswer.setVisibility(View.VISIBLE);
        lineShowAnswer.setVisibility(View.VISIBLE);
    }

    @Override
    public void onResume(){
        super.onResume();

    }
    @Override
    public void onPause(){
        super.onPause();

    }


}


