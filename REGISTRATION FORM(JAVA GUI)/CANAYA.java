package files;

/*Berndt Dennis F. Canaya GWAPO*/
import java.awt.*;
import javax.swing.*;

public class CANAYA {

	public static void main(String[] args) {
		JFrame frame = new JFrame("REGISTRATION FORM");

		JPanel panel = new JPanel();

		JLabel title = new JLabel("REGISTRATION FORM");
		JLabel name = new JLabel("Name                   : ");
		JLabel mobile_num = new JLabel("Mobile Number    : ");
		JLabel gender = new JLabel("Gender                : ");
		JLabel address = new JLabel("Address               : ");
		JLabel male = new JLabel("MALE");
		JLabel female = new JLabel("FEMALE");
		JLabel terms_and_conditions = new JLabel("Accept Terms and Conditions");

		JTextField name_field = new JTextField();
		JTextField mobile_num_field = new JTextField();
		JTextField address_field = new JTextField();

		JRadioButton gender_male_radioButton = new JRadioButton();
		JRadioButton gender_female_radioButton = new JRadioButton();

		JCheckBox checkBox = new JCheckBox();

		JButton submit = new JButton("Submit");
		JButton reset = new JButton("Reset");

		ButtonGroup choices = new ButtonGroup();

		frame.setLayout(null);
		frame.setVisible(true);
		frame.setSize(750, 450);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.add(title);
		frame.add(name);
		frame.add(name_field);
		frame.add(mobile_num);
		frame.add(mobile_num_field);
		frame.add(gender);
		frame.add(gender_male_radioButton);
		frame.add(male);
		frame.add(gender_female_radioButton);
		frame.add(female);
		frame.add(address);
		frame.add(address_field);
		frame.add(checkBox);
		frame.add(terms_and_conditions);
		frame.add(submit);
		frame.add(reset);
		frame.add(panel);

		panel.setBackground(Color.black);
		panel.setBounds(0, 0, 750, 500);

		title.setForeground(Color.white);
		title.setBounds(250, 25, 450, 30);
		title.setFont(new Font("Sans", Font.BOLD, 20));

		name.setForeground(Color.WHITE);
		name.setBounds(50, 100, 200, 20);
		name.setFont(new Font("Sans", Font.BOLD, 20));

		name_field.setBounds(250, 90, 325, 30);
		name_field.setFont(new Font("Sans", Font.BOLD, 20));

		mobile_num.setForeground(Color.white);
		mobile_num.setBounds(50, 150, 200, 20);
		mobile_num.setFont(new Font("Sans", Font.BOLD, 20));

		mobile_num_field.setBounds(250, 140, 325, 30);
		mobile_num_field.setFont(new Font("Sans", Font.BOLD, 20));

		gender.setForeground(Color.white);
		gender.setBounds(50, 200, 200, 20);
		gender.setFont(new Font("Sans", Font.BOLD, 20));

		gender_male_radioButton.setBounds(250, 200, 20, 20);
		gender_male_radioButton.setBackground(Color.black);

		male.setBounds(275, 200, 50, 20);
		male.setForeground(Color.white);
		male.setFont(new Font("Sans", Font.BOLD, 17));

		gender_female_radioButton.setBounds(375, 200, 20, 20);
		gender_female_radioButton.setBackground(Color.black);

		female.setBounds(400, 200, 100, 20);
		female.setForeground(Color.WHITE);
		female.setFont(new Font("Sans", Font.BOLD, 17));

		choices.add(gender_male_radioButton);
		choices.add(gender_female_radioButton);

		address.setForeground(Color.white);
		address.setBounds(50, 250, 200, 20);
		address.setFont(new Font("Sans", Font.BOLD, 20));

		address_field.setBounds(250, 240, 325, 30);
		address_field.setFont(new Font("Sans", Font.BOLD, 20));

		checkBox.setBounds(135, 300, 20, 20);
		checkBox.setBackground(Color.black);

		terms_and_conditions.setBounds(170, 300, 300, 20);
		terms_and_conditions.setFont(new Font("Sans", Font.ITALIC, 14));
		terms_and_conditions.setForeground(Color.white);

		submit.setBounds(225, 350, 100, 30);
		submit.setForeground(Color.blue);
		submit.setFont(new Font("Sans", Font.BOLD, 15));

		reset.setBounds(350, 350, 100, 30);
		reset.setForeground(Color.blue);
		reset.setFont(new Font("Sans", Font.BOLD, 15));
		
	}

}