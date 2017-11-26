package bgu.psyacad.adapters;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Filter;
import android.widget.LinearLayout;
import android.widget.TextView;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import bgu.psyacad.R;
import bgu.psyacad.core.Word;

/**
 * Created by ilayeliashar on 07/01/2016.
 */
public class AutoCompleteAdapter extends ArrayAdapter<Word> implements Serializable{
    Context context;
    int resource, textViewResourceId;
    List<Word> items, tempItems, suggestions;

    public AutoCompleteAdapter(Context context, int resource, int textViewResourceId, List<Word> items){
        super(context, resource, textViewResourceId, items);
        this.context = context;
        this.resource = resource;
        this.textViewResourceId = textViewResourceId;
        this.items = items;
        tempItems = new ArrayList<Word>(items); // this makes the difference.
        suggestions = new ArrayList<Word>();
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {

        View view = convertView;
        if (convertView == null) {
            LayoutInflater inflater = (LayoutInflater) context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
            view = inflater.inflate(R.layout.list_view, parent, false);
        }

        // @param people is the word, have no idea why I chose people

        Word people = items.get(position);
        if (people != null) {
            LinearLayout layout=(LinearLayout) view.findViewById(R.id.wordViewLinear);
            TextView lblName = (TextView) view.findViewById(R.id.wordListView);
            if (lblName != null) lblName.setText(people.getWord());


        }
        return view;
    }

    @Override
    public Filter getFilter() {
        return nameFilter;
    }

    /**
     * Custom Filter implementation for custom suggestions we provide.
     */

    Filter nameFilter = new Filter() {
        @Override
        public CharSequence convertResultToString(Object resultValue) {
            String str = ((Word) resultValue).getWord();
            return str;
        }

        @Override
        protected FilterResults performFiltering(CharSequence constraint) {
            if (constraint != null) {
                suggestions.clear();
                for (Word people : tempItems) {
                    if (people.getWord().toLowerCase().contains(constraint.toString().toLowerCase())) {
                        suggestions.add(people);
                    }
                }
                FilterResults filterResults = new FilterResults();
                filterResults.values = suggestions;
                filterResults.count = suggestions.size();
                return filterResults;
            } else {
                return new FilterResults();
            }
        }

        @Override
        protected void publishResults(CharSequence constraint, FilterResults results) {
            List<Word> filterList = (ArrayList<Word>) results.values;
            if (results != null && results.count > 0) {
                clear();
                for (Word people : filterList) {
                    add(people);
                    notifyDataSetChanged();
                }
            }
        }
    };
}
