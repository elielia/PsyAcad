package bgu.psyacad.service;

import android.app.Service;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Binder;
import android.os.Handler;
import android.os.IBinder;
import android.preference.PreferenceManager;
import android.widget.Toast;

import com.google.gson.Gson;

import bgu.psyacad.util.DataHolder;

public class SavingService extends Service {
    private final LocalBinder mBinder = new LocalBinder();
    protected Handler handler;
    protected Toast mToast;

    public class LocalBinder extends Binder {
        public SavingService getService() {
            return SavingService.this;
        }
    }

    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }

    @Override
    public void onCreate() {
        super.onCreate();

    }

    @Override
    public void onDestroy() {
        super.onDestroy();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {

        Gson gson = new Gson();
        String words_string = gson.toJson(DataHolder.words);
        String known_english = gson.toJson(DataHolder.knownEnglish);
        String main_queue_english = gson.toJson(DataHolder.mainQueueEnglish);
        String seen_queue_english = gson.toJson(DataHolder.seenQueueEnglish);

        String known_hebrew = gson.toJson(DataHolder.knownHebrew);
        String main_queue_hebrew = gson.toJson(DataHolder.mainQueueHebrew);
        String seen_queue_hebrew = gson.toJson(DataHolder.seenQueueHebrew);

        if (!words_string.equals("null")) {
            SharedPreferences preferences = PreferenceManager.getDefaultSharedPreferences(this);
            SharedPreferences.Editor preferencesEditor = preferences.edit();

                preferencesEditor.putString("words", words_string);
                preferencesEditor.putString("known_english", known_english);
                preferencesEditor.putString("main_queue_english", main_queue_english);
                preferencesEditor.putString("seen_queue_english", seen_queue_english);
                preferencesEditor.putString("known_hebrew", known_hebrew);
                preferencesEditor.putString("main_queue_hebrew", main_queue_hebrew);
                preferencesEditor.putString("seen_queue_hebrew", seen_queue_hebrew);
                preferencesEditor.commit();


        }
        return 0;
    }

}
