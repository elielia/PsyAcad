package bgu.psyacad.util;

import android.content.SharedPreferences;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.lang.reflect.Type;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Queue;

import bgu.psyacad.core.Word;

/**
 * Created by ilayeliashar on 08/02/2016.
 */
public class DataHolder{



    public static ArrayList<Word> words;
    public static ArrayList<Word> knownEnglish;
    public static ArrayList<Word> knownHebrew;
    public static ArrayDeque<Word> mainQueueEnglish,mainQueueHebrew;
    public static PriorityQueue<Word> seenQueueEnglish,seenQueueHebrew;
    public static int numOfEnglishWords;
    public static int numOfHebrewWords;

    public static void initData(SharedPreferences preferences){

        words=initWords(preferences);
        initEnglish(preferences);
        initHebrew(preferences);
    }

    private static void initHebrew(SharedPreferences preferences) {
        knownHebrew=initKnownHebrew(preferences);
        mainQueueHebrew=initMainQueueHebrew(preferences);
        seenQueueHebrew=initSeenQueueHebrew(preferences);
        numOfHebrewWords = preferences.getInt(Constants.NUM_OF_HEBREW_WORDS,0);
    }

    private static void initEnglish(SharedPreferences preferences) {
        knownEnglish=initKnownEnglish(preferences);
        mainQueueEnglish=initMainQueueEnglish(preferences);
        seenQueueEnglish=initSeenQueueEnglish(preferences);
        numOfEnglishWords = preferences.getInt(Constants.NUM_OF_ENGLISH_WORDS,0);
    }


    private static ArrayList<Word> initWords(SharedPreferences preferences) {
        Gson gson=new Gson();

        String words_array = preferences.getString(Constants.WORDS, Constants.EMPTY_STRING);
        Type type = new TypeToken<List<Word>>(){}.getType();
        ArrayList<Word> words = gson.fromJson(words_array, type);
        return words;
    }

    private static ArrayList<Word> initKnownEnglish(SharedPreferences preferences) {

        Gson gson=new Gson();

        String known_english_array = preferences.getString(Constants.KNOWN_ENGLISH,Constants.EMPTY_STRING);
        Type type = new TypeToken<List<Word>>(){}.getType();
        ArrayList<Word> known_english = gson.fromJson(known_english_array, type);

        return known_english;

    }

    private static ArrayDeque<Word> initMainQueueEnglish(SharedPreferences preferences) {

        Gson gson=new Gson();

        String main_queue = preferences.getString(Constants.MAIN_QUEUE_ENGLISH,Constants.EMPTY_STRING);
        Type type = new TypeToken<Queue<Word>>(){}.getType();
        ArrayDeque<Word> mainQueue = gson.fromJson(main_queue, type);

        return mainQueue;
    }

    private static PriorityQueue<Word> initSeenQueueEnglish(SharedPreferences preferences) {

        Gson gson=new Gson();

        String seen_queue = preferences.getString(Constants.SEEN_QUEUE_ENGLISH,Constants.EMPTY_STRING);
        Type type = new TypeToken<PriorityQueue<Word>>(){}.getType();
        PriorityQueue<Word> seenQueue = gson.fromJson(seen_queue, type);

        return seenQueue;


    }

    private static ArrayList<Word> initKnownHebrew(SharedPreferences preferences) {

        Gson gson=new Gson();

        String known_hebrew_array = preferences.getString(Constants.KNOWN_HEBREW,Constants.EMPTY_STRING);
        Type type = new TypeToken<List<Word>>(){}.getType();
        ArrayList<Word> known_hebrew = gson.fromJson(known_hebrew_array, type);

        return known_hebrew;

    }

    private static ArrayDeque<Word> initMainQueueHebrew(SharedPreferences preferences) {

        Gson gson=new Gson();

        String main_queue = preferences.getString(Constants.MAIN_QUEUE_HEBREW,Constants.EMPTY_STRING);
        Type type = new TypeToken<Queue<Word>>(){}.getType();
        ArrayDeque<Word> mainQueue = gson.fromJson(main_queue, type);

        return mainQueue;
    }

    private static PriorityQueue<Word> initSeenQueueHebrew(SharedPreferences preferences) {

        Gson gson = new Gson();

        String seen_queue = preferences.getString(Constants.SEEN_QUEUE_HEBREW, Constants.EMPTY_STRING);
        Type type = new TypeToken<PriorityQueue<Word>>() {
        }.getType();
        PriorityQueue<Word> seenQueue = gson.fromJson(seen_queue, type);

        return seenQueue;

    }

    public static void setWordIsKnown(int index, boolean bool){
        words.get(index).setKnowIt(bool);
    }


}
