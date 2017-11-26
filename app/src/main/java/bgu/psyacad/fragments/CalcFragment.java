package bgu.psyacad.fragments;

import android.graphics.Typeface;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.Spinner;
import android.widget.TextView;

import bgu.psyacad.R;
import bgu.psyacad.grades.CalcGrade;
import bgu.psyacad.grades.SimulationGrade;

/**
 * Created by ilayeliashar on 02/01/2016.
 */
public class CalcFragment extends Fragment {


    public static final String EMPTY_STRING = "";
    public static final String NOTO_SANS_HEBREW_BOLD_PATH = "fonts/NotoSansHebrew-Bold.ttf";
    public static final String NOTO_SANS_HEBREW_REGULAR_PATH = "fonts/NotoSansHebrew-Regular.ttf";

    @Nullable
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view= inflater.inflate(R.layout.calc_layout,container,false);
        TextView grade=(TextView) view.findViewById(R.id.gradeCalcView);
        Typeface NotoSansHerbrewRegular = Typeface.createFromAsset(getActivity().getAssets(), NOTO_SANS_HEBREW_BOLD_PATH);
        grade.setTypeface(NotoSansHerbrewRegular);
        Typeface NotoSansHerbrewBold = Typeface.createFromAsset(getActivity().getAssets(), NOTO_SANS_HEBREW_REGULAR_PATH);
        grade.setTypeface(NotoSansHerbrewBold);

        final EditText verbalGrade=(EditText) view.findViewById(R.id.miluli1);
        final EditText contentGrade=(EditText) view.findViewById(R.id.miluli2);
        final EditText languageGrade=(EditText) view.findViewById(R.id.miluli3);
        final EditText quantitiveGrade=(EditText) view.findViewById(R.id.kamuti);
        final EditText englishGrade=(EditText) view.findViewById(R.id.anglit);
        final Spinner simulationDate=(Spinner) view.findViewById(R.id.simulation);
        final ImageView line=(ImageView) view.findViewById(R.id.lineee);
        final ImageView restart = (ImageView) view.findViewById(R.id.restartButton);
        final TextView generalGrade = (TextView) view.findViewById(R.id.generalGrade);
        final TextView otherGrades = (TextView) view.findViewById(R.id.otherGrades);
        final Button calculate=(Button) view.findViewById(R.id.calculateButton);

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this.getActivity(), R.layout.simulation_spinner_item, getResources().getStringArray(R.array.simulationDates));
        adapter.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        simulationDate.setAdapter(adapter);

        restart.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                verbalGrade.setText(EMPTY_STRING);
                contentGrade.setText(EMPTY_STRING);
                languageGrade.setText(EMPTY_STRING);
                quantitiveGrade.setText(EMPTY_STRING);
                englishGrade.setText(EMPTY_STRING);
                simulationDate.setSelection(0);

                generalGrade.setText(EMPTY_STRING);
                otherGrades.setText(EMPTY_STRING);
                calculate.setVisibility(View.VISIBLE);
                line.setVisibility(View.VISIBLE);
            }
        });


        calculate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                int simulationNum = calculateSimulationFromDate(simulationDate);

                cleanRedBorders(verbalGrade, contentGrade, languageGrade, quantitiveGrade, englishGrade);

                boolean isFilled = true;

                int simNum;
                double english, quantitive, verbal, content, language;

                if (isEmptyEditText(verbalGrade) || Double.parseDouble(languageGrade.getText().toString())>46){
                    verbalGrade.setBackgroundResource(R.drawable.edit_text_shape_red_stroke);
                    isFilled = false;
                }
                if (isEmptyEditText(contentGrade) || Double.parseDouble(contentGrade.getText().toString())>6){
                    contentGrade.setBackgroundResource(R.drawable.edit_text_shape_red_stroke);
                    isFilled = false;
                }
                if (isEmptyEditText(languageGrade) || Double.parseDouble(languageGrade.getText().toString())>6){
                    languageGrade.setBackgroundResource(R.drawable.edit_text_shape_red_stroke);
                    isFilled = false;
                }
                if (isEmptyEditText(quantitiveGrade) || Double.parseDouble(quantitiveGrade.getText().toString())>40){
                    quantitiveGrade.setBackgroundResource(R.drawable.edit_text_shape_red_stroke);
                    isFilled = false;
                }
                if (isEmptyEditText(englishGrade) || Double.parseDouble(englishGrade.getText().toString())>48){
                    englishGrade.setBackgroundResource(R.drawable.edit_text_shape_red_stroke);
                    isFilled = false;
                }

                if (!isFilled)
                    return;

                //cleanRedBorders(verbalGrade, contentGrade, languageGrade, quantitiveGrade, englishGrade, simulationNum);

                english = Double.parseDouble(englishGrade.getText().toString());
                quantitive = Double.parseDouble(quantitiveGrade.getText().toString());
                verbal = Double.parseDouble(verbalGrade.getText().toString());
                content = Double.parseDouble(contentGrade.getText().toString());
                language = Double.parseDouble(languageGrade.getText().toString());



                SimulationGrade res = CalcGrade.getGrade(simulationNum, english, quantitive, verbal, language, content);
                generalGrade.setText("ציון פסיכומטרי: " + res.getGeneral_grade());
                otherGrades.setText( "דגש כמותי: "+res.getQ_grade()+ "\nדגש מילולי: " + res.getV_grade());
                calculate.setVisibility(View.INVISIBLE);
                line.setVisibility(View.INVISIBLE);
                
            }
        });

        return view;

    }

    private int calculateSimulationFromDate(Spinner simulationDate) {

        return simulationDate.getSelectedItemPosition()+19;
    }

    private void cleanRedBorders(EditText verbalGrade, EditText contentGrade, EditText languageGrade, EditText quantitiveGrade, EditText englishGrade) {
        verbalGrade.setBackgroundResource(R.drawable.edit_text_shape);
        contentGrade.setBackgroundResource(R.drawable.edit_text_shape);
        languageGrade.setBackgroundResource(R.drawable.edit_text_shape);
        quantitiveGrade.setBackgroundResource(R.drawable.edit_text_shape);
        englishGrade.setBackgroundResource(R.drawable.edit_text_shape);
    }


    private boolean isEmptyEditText(EditText toCheck){
        String s=toCheck.getText().toString();
        return s.matches(EMPTY_STRING);

    }
}
