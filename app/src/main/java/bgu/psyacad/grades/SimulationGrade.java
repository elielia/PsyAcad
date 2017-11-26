package bgu.psyacad.grades;

/**
 * Created by ilayeliashar on 16/09/2017.
 */
public class SimulationGrade {



    private int general_grade;
    private int q_grade;
    private int v_grade;

    public SimulationGrade(double general_grade,double q_grade, double v_grade){

        this.general_grade = (int)general_grade;
        this.q_grade = (int)q_grade;
        this.v_grade = (int)v_grade;

    }


    public int getV_grade() {
        return v_grade;
    }

    public int getQ_grade() {
        return q_grade;
    }

    public int getGeneral_grade() {
        return general_grade;
    }
}
