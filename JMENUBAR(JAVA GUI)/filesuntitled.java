package files;

import java.awt.*;
import javax.swing.*;
/*BERNDT DENNIS FABIAN CANAYA*/
public class filesuntitled {

	public static void main(String[] args) {
		
		JFrame frame = new JFrame();
		
		JMenuBar menu_bar = new JMenuBar();
		
		JMenu file = new JMenu();
		JMenu edit = new JMenu();
		JMenu view = new JMenu();
		JMenu tools = new JMenu();
		JMenu help = new JMenu();
		
		JMenuItem New = new JMenuItem("New                             CTRL+N");
		JMenuItem open = new JMenuItem("Open                           CTRL+O");
		JMenuItem save= new JMenuItem("Save                            CTRL+S");
		JMenuItem save_as = new JMenuItem("Save as...");
		
		ImageIcon icon = new ImageIcon();
		
		JSeparator separator1 = new JSeparator();
		JSeparator separator2 = new JSeparator();
		
		JMenuItem page_setup = new JMenuItem("Page Setup...");
		JMenuItem print = new JMenuItem("Print...                         CTRL+P");
		
		JMenuItem exit = new JMenuItem("Exit");
		
		
		frame.setTitle("Untitled - My Files");
		frame.setSize(890, 560);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLayout(null);
		frame.setVisible(true);
		frame.add(menu_bar);
		
		menu_bar.setSize(890, 35);
		menu_bar.setBackground(Color.white);
		menu_bar.add(file);
		menu_bar.add(edit);
		menu_bar.add(view);
		menu_bar.add(tools);
		menu_bar.add(help);
		
		file.setText("File");
		file.setForeground(Color.black);
		file.setFont(new Font("Sans", Font.PLAIN, 15));
		file.add(New);
		file.add(open);
		file.add(save);
		file.add(save_as);
		file.add(separator1);
		file.add(page_setup);
		file.add(print);
		file.add(separator2);
		file.add(exit);
		
		New.setSize(200, 20);
		
		open.setSize(200, 20);
		
		save.setSize(200, 20);
		
		save_as.setSize(200, 20);
		
		page_setup.setSize(200, 20);
		
		print.setSize(200, 20);
		
		exit.setSize(200, 20);
		
		edit.setText("Edit");
		edit.setForeground(Color.black);
		edit.setFont(new Font("Sans", Font.PLAIN, 15));
		
		view.setText("View");
		view.setForeground(Color.black);
		view.setFont(new Font("Sans", Font.PLAIN, 15));
		
		tools.setText("Tools");
		tools.setForeground(Color.black);
		tools.setFont(new Font("Sans", Font.PLAIN, 15));
		
		help.setText("Help");
		help.setForeground(Color.black);
		help.setFont(new Font("Sans", Font.PLAIN, 15));	
	}

}
