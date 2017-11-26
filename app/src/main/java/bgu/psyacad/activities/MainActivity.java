package bgu.psyacad.activities;

import android.app.ActionBar;
import android.app.AlertDialog;
import android.app.Dialog;
import android.app.FragmentTransaction;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.graphics.Typeface;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.design.widget.TabLayout;
import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.SearchView;
import android.support.v7.widget.Toolbar;
import android.view.LayoutInflater;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.WindowManager;
import android.view.inputmethod.InputMethodManager;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import java.io.IOException;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.Date;
import java.util.PriorityQueue;
import java.util.Queue;

import bgu.psyacad.R;
import bgu.psyacad.adapters.AutoCompleteAdapter;
import bgu.psyacad.adapters.CustomAdapter;
import bgu.psyacad.core.Word;
import bgu.psyacad.service.SavingService;
import bgu.psyacad.util.DataHolder;
import bgu.psyacad.util.PsyUtils;


public class MainActivity extends AppCompatActivity implements ActionBar.TabListener {
    private TabLayout tabLayout;
    private ViewPager viewPager;
    private ArrayList<Word> words,known;
    private PriorityQueue<Word> seenQueue;
    private Queue<Word> mainQueue;
    public static AutoCompleteAdapter adapter;
    private android.support.v7.widget.ActionMenuView stats;
    //private boolean resumed=true;
    private Typeface type;
    //private boolean usingWords = false;

    /**
     *
     * @param savedInstanceState
     */


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity_tabs);

        tabLayout = (TabLayout) findViewById(R.id.tab_layout);
        viewPager = (ViewPager) findViewById(R.id.pager);
        viewPager.setAdapter(new CustomAdapter(getSupportFragmentManager(), getApplicationContext()));
        tabLayout.setupWithViewPager(viewPager);

        //// SVG -- check with mom
        tabLayout.getTabAt(0).setIcon(R.drawable.a_icon_active);
        tabLayout.getTabAt(1).setIcon(R.drawable.alefff);
        tabLayout.getTabAt(2).setIcon(R.drawable.calc_gray);
        tabLayout.getTabAt(3).setIcon(R.drawable.info_icon);


        DataHolder.initData(PreferenceManager.getDefaultSharedPreferences(this));

        // Upper Toolbar, buttons are in the menu_main.xml file under menu folder

        Toolbar myToolbar = (Toolbar) findViewById(R.id.my_toolbar);
        TextView toolbar_title=(TextView) findViewById(R.id.toolbar_title);

        stats= (android.support.v7.widget.ActionMenuView) findViewById(R.id.statsButton);


        type = Typeface.createFromAsset(getAssets(),"fonts/Alef-Regular.ttf");
        toolbar_title.setTypeface(type);

        setSupportActionBar(myToolbar);
        getSupportActionBar().setDisplayShowTitleEnabled(false);
        myToolbar.getMenu().clear();

        adapter=new AutoCompleteAdapter(this, R.layout.search_dialog, R.id.wordListView, DataHolder.words);
        adapter.notifyDataSetChanged();

        // the tabs menu

        tabLayout.setOnTabSelectedListener(new TabLayout.OnTabSelectedListener() {
            @Override
            public void onTabSelected(TabLayout.Tab tab) {

                hideKeyboard();

                viewPager.setCurrentItem(tab.getPosition());
                if (tab.getPosition()==0) tab.setIcon(R.drawable.a_icon_active);
                else if (tab.getPosition()==1) tab.setIcon(R.drawable.alef_icon_active);
                else if (tab.getPosition()==2) tab.setIcon(R.drawable.calc_active);
                else if (tab.getPosition()==3) tab.setIcon(R.drawable.info2);

            }

            @Override
            public void onTabUnselected(TabLayout.Tab tab) {
                if (tab.getPosition()==0) tab.setIcon(R.drawable.a_icon);
                else if (tab.getPosition()==1) tab.setIcon(R.drawable.alefff);
                else if (tab.getPosition()==2) tab.setIcon(R.drawable.calc_gray);
                else if (tab.getPosition()==3) tab.setIcon(R.drawable.info_icon);

            }

            @Override
            public void onTabReselected(TabLayout.Tab tab) {
                // viewPager.setCurrentItem(tab.getPosition());
                if (tab.getPosition()==0) tab.setIcon(R.drawable.a_icon_active);
                else if (tab.getPosition()==1) tab.setIcon(R.drawable.alef_icon_active);
                else if (tab.getPosition()==2) tab.setIcon(R.drawable.calc_active);
                else if (tab.getPosition()==3) tab.setIcon(R.drawable.info2);
            }
        });

        // Statistics button, THE OTHER BUTTON (SEARCH) IS IN menu_.xml

        stats.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                    LayoutInflater inflater = getLayoutInflater();

                    // Opens a new dialog, gets the listview and the searchview, and filters results

                    Dialog dialog = new Dialog(MainActivity.this);
                    AlertDialog.Builder builder = new AlertDialog.Builder(MainActivity.this);
                    View view = inflater.inflate(R.layout.stats_layout, null);
                    TextView title = (TextView) view.findViewById(R.id.statsTitle);
                    TextView englishLeft = (TextView) view.findViewById(R.id.englishLeft);
                    TextView hebrewLeft = (TextView) view.findViewById(R.id.hebrewLeft);
                    TextView averageAday = (TextView) view.findViewById(R.id.averageAday);

                    title.setTypeface(type);
                    NumberFormat per=NumberFormat.getPercentInstance();
                    englishLeft.setText("" +per.format((double) (DataHolder.knownEnglish.size()) / DataHolder.numOfEnglishWords));
                    hebrewLeft.setText("" +per.format((double) (DataHolder.knownHebrew.size()) / DataHolder.numOfHebrewWords));

                    PackageInfo packageInfo = null;
                    try {
                        PackageManager pm = getBaseContext().getPackageManager();
                        packageInfo = pm.getPackageInfo("bgu.psyacad", PackageManager.GET_PERMISSIONS);
                        Date installTime = new Date(packageInfo.firstInstallTime);
                        int difference = (int) getDifference(installTime, new Date());
                        long average = (DataHolder.knownEnglish.size() + DataHolder.knownHebrew.size()) / (difference + 1);
                        averageAday.setText(""+(int) average);

                    } catch (PackageManager.NameNotFoundException e) {
                        e.printStackTrace();
                    }

                    builder.setView(view);
                    dialog = builder.create();
                    dialog.show();
                }


        });

    }



    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        // Happenes when clicking the search button

        if (id==R.id.searchButton){

            LayoutInflater inflater = getLayoutInflater();

            // Opens a new dialog, gets the listview and the searchview, and filters results

            Dialog dialog = new Dialog(this);
            dialog.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_DIM_BEHIND);
            AlertDialog.Builder builder = new AlertDialog.Builder(this);
            View view=inflater.inflate(R.layout.search_dialog,null);
            ListView list=(ListView) view.findViewById(R.id.searchlistView);
            SearchView searchbar= (SearchView) view.findViewById(R.id.searchbar);


            list.setAdapter(adapter);
            adapter.notifyDataSetChanged();
            searchbar.setIconifiedByDefault(false);
            searchbar.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
                @Override
                public boolean onQueryTextSubmit(String query) {
                    return false;
                }

                @Override
                public boolean onQueryTextChange(String newText) {
                    adapter.getFilter().filter(newText);
                    return false;
                }
            });

            // When clicking on a searched word

            final Dialog finalDialog = dialog;

            list.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                    Word clickedWord = DataHolder.words.get((int) id);

                    // hide dialog keyboard
                    InputMethodManager in = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
                    in.hideSoftInputFromWindow(view.getWindowToken(), 0);
                    openSecondDialog(clickedWord);


                }
            });


            builder.setView(view);
            dialog = builder.create();
            dialog.show();




        }

        return super.onOptionsItemSelected(item);
    }

    //ch


    @Override
    public void onTabSelected(ActionBar.Tab tab, FragmentTransaction ft) {

    }

    @Override
    public void onTabUnselected(ActionBar.Tab tab, FragmentTransaction ft) {

    }

    @Override
    public void onTabReselected(ActionBar.Tab tab, FragmentTransaction ft) {

    }



    public long getDifference(Date startDate, Date endDate){

        //milliseconds
        long different = endDate.getTime() - startDate.getTime();

        long secondsInMilli = 1000;
        long minutesInMilli = secondsInMilli * 60;
        long hoursInMilli = minutesInMilli * 60;
        long daysInMilli = hoursInMilli * 24;

        long elapsedDays = different / daysInMilli;
        different = different % daysInMilli;

        return elapsedDays;
    }

    public void openSecondDialog(final Word word){



        LayoutInflater inflater = getLayoutInflater();

        Typeface type = Typeface.createFromAsset(getAssets(),"fonts/Alef-Regular.ttf");
        Typeface type2 = Typeface.createFromAsset(getAssets(), "fonts/NotoSansHebrew-Regular.ttf");

        // Opens a new dialog, gets the listview and the searchview, and filters results

        AlertDialog.Builder builder = new AlertDialog.Builder(this);

        View view;

        view=inflater.inflate(R.layout.searched_word_layout_english,null);
        TextView wordView=(TextView) view.findViewById(R.id.searchedWordView);
        TextView wordTransView = (TextView) view.findViewById(R.id.searchedTransWordView);
        TextView wordDescView = (TextView) view.findViewById(R.id.searchedDescWordView);

        ImageButton sound=(ImageButton) view.findViewById(R.id.soundButton);

        sound.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                try {
                    if (word != null) {
                        MediaPlayer mediaPlayer = MediaPlayer.create(getApplicationContext(), PsyUtils.getId("sound" + String.valueOf(word.getId())));
                        if (mediaPlayer != null)
                            mediaPlayer.start();
                    }
                } catch (RuntimeException e){
                    System.out.println("There is no sound for this word");
                }
            }
        });

        ImageView studied=(ImageView) view.findViewById(R.id.studiedImage);
        TextView studiedText=(TextView) view.findViewById(R.id.studiedText);

        //ImageView wordImage=(ImageView) view.findViewById(R.id.searchedImageWord);

        if (word.isKnowIt()) {
            studied.setImageResource(R.drawable.v_icon_new);
            studiedText.setText("המילה נלמדה");
        }
        else {
            studied.setImageResource(R.drawable.x_icon_new);
            studiedText.setText("המילה לא נלמדה");
        }

        wordView.setTypeface(type);
        wordTransView.setTypeface(type2);
        wordDescView.setTypeface(type2);

        wordView.setText(word.getWord());
        wordTransView.setText(word.getTranslation());
        wordDescView.setText(word.getDescription());


        Button backButton=(Button) view.findViewById(R.id.backButton);

        builder.setView(view);
        final Dialog dialog = builder.create();
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                dialog.dismiss();
            }
        });

        WindowManager.LayoutParams lp = dialog.getWindow().getAttributes();
        lp.dimAmount=0.0f; // Dim level. 0.0 - no dim, 1.0 - completely opaque
        dialog.getWindow().setAttributes(lp);
        dialog.getWindow().clearFlags(WindowManager.LayoutParams.FLAG_DIM_BEHIND);

        dialog.show();

    }

    private void hideKeyboard(){

        View view = this.getCurrentFocus();
        if (view != null) {
            InputMethodManager imm = (InputMethodManager) getSystemService(Context.INPUT_METHOD_SERVICE);
            imm.hideSoftInputFromWindow(view.getWindowToken(), 0);
        }
    }


    private void save() throws IOException {

        startService(new Intent(this, SavingService.class));
    }


    @Override
    public void onPause(){
        super.onPause();
        try {
            save();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onSaveInstanceState(Bundle outState){

        outState.clear();
        super.onSaveInstanceState(outState);
    }




}

