package bgu.psyacad.util;

import java.lang.reflect.Field;
import java.util.Calendar;
import java.util.Date;

import bgu.psyacad.R;

/**
 * Created by ilayeliashar on 21/03/2017.
 */
public class PsyUtils {

    public static Date getCurrentDate(){

        Calendar c = Calendar.getInstance();

        // set the calendar to start of today
        c.set(Calendar.HOUR_OF_DAY, 0);
        c.set(Calendar.MINUTE, 0);
        c.set(Calendar.SECOND, 0);
        c.set(Calendar.MILLISECOND, 0);

        return c.getTime();
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
}
