package bgu.psyacad.core;

import java.io.Serializable;
import java.util.Calendar;
import java.util.Date;

/**
 * Created by ilayeliashar on 02/01/2016.
 */
public class Word implements Comparable,Serializable {

    private String word;
    private String description;
    private String translation;
    private int id;
    private Date nextDate;
    private int timesSeen;
    private double EF;
    private int previousInterval;
    boolean knowIt;


    public Word(int id,String word, String translation, String description){

        this.word=word;
        this.description=description;
        this.translation=translation;
        this.id=id;
        nextDate=new Date();
        timesSeen=1;
        EF=2.2;
        previousInterval=1;
        knowIt=false;


    }


    public Date getNextDate() {
        return nextDate;
    }
    public String getWord() {
        return word;
    }

    public String getTranslation() {
        return translation;
    }


    public String getDescription() {
        return description;
    }

    public int getId() {
        return id;
    }


    @Override
    public int compareTo(Object another) {
        Word other=(Word) another;
        if (this.getNextDate().before(other.getNextDate())) return -1;
        else if(this.getNextDate().equals(((Word) another).getNextDate())) return 0;
        return 1;
    }
    public int getTimesSeen(){
        return timesSeen;
    }
    public void increaseTimesSeen(){
        timesSeen++;
    }
    public double getEF(){
        return EF;
    }
    public void setEF(double newEF){
        EF=newEF;
    }

    public void setDateBy(int x){

        Calendar c=Calendar.getInstance();
        System.out.println("the previous nextDate of the word "+getWord()+" was "+getNextDate().toString());
        c.add(Calendar.DATE, x);
        nextDate=c.getTime();
        System.out.println("the new nextDate of the word " + getWord() + " is " + getNextDate().toString());

    }
    public int getPreviousInterval() {
        return previousInterval;
    }

    public void setPreviousInterval(int previousInterval) {
        this.previousInterval = previousInterval;
    }


    public boolean isKnowIt() {
        return knowIt;
    }

    public void setKnowIt(boolean knowIt) {
        this.knowIt = knowIt;
    }



}
