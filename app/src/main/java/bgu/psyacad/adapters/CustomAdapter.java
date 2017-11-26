package bgu.psyacad.adapters;

import android.content.Context;
import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentPagerAdapter;

import bgu.psyacad.fragments.CalcFragment;
import bgu.psyacad.fragments.InfoFragment;
import bgu.psyacad.fragments.LanguageFragment;
import bgu.psyacad.util.Constants;
import bgu.psyacad.util.DataHolder;

/**
 * Created by ilayeliashar on 02/01/2016.
 */
public class CustomAdapter extends FragmentPagerAdapter {

    public static final String KNOWN_WORDS = "knownWords";
    public static final String MAIN_QUEUE = "mainQueue";
    public static final String SEEN_QUEUE = "seenQueue";

    private String[] fragments={"","","",""};

    public CustomAdapter(FragmentManager supportFragmentManager, Context applicationContext) {
        super(supportFragmentManager);
    }

    @Override
    public Fragment getItem(int position) {
        switch (position){
            case 0:

                LanguageFragment englishFragment = new LanguageFragment();
                Bundle englishArgs = new Bundle();
                englishArgs.putSerializable(KNOWN_WORDS, DataHolder.knownEnglish);
                englishArgs.putSerializable(MAIN_QUEUE, DataHolder.mainQueueEnglish);
                englishArgs.putSerializable(SEEN_QUEUE, DataHolder.seenQueueEnglish);
                englishFragment.setArguments(englishArgs);
                return englishFragment;

            case 1:
                LanguageFragment hebrewFragment = new LanguageFragment();
                Bundle hebrewArgs = new Bundle();
                hebrewArgs.putSerializable(KNOWN_WORDS, DataHolder.knownHebrew);
                hebrewArgs.putSerializable(MAIN_QUEUE, DataHolder.mainQueueHebrew);
                hebrewArgs.putSerializable(SEEN_QUEUE, DataHolder.seenQueueHebrew);
                hebrewFragment.setArguments(hebrewArgs);
                return hebrewFragment;

            case 2:
                return new CalcFragment();
            case 3:
                return new InfoFragment();

        }
        return null;
    }

    @Override
    public int getCount() {
        return 4;
    }

    @Override
    public CharSequence getPageTitle(int position) {
        return Constants.EMPTY_STRING;

    }
}
