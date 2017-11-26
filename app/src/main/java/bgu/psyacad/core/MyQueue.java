package bgu.psyacad.core;

import java.io.Serializable;
import java.util.concurrent.ArrayBlockingQueue;

/**
 * Created by ilayeliashar on 10/09/2016.
 */
public class MyQueue<E> extends ArrayBlockingQueue implements Serializable{

    public MyQueue(int size){
        super(size);
    }
}

