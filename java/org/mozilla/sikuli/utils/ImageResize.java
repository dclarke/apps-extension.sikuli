package org.mozilla.sikuli.utils;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class ImageResize {
 
	private static final int IMG_WIDTH = 70;
	private static final int IMG_HEIGHT = 63;
  
  public ImageResize(String filename)  {
    try{
      BufferedImage originalImage = ImageIO.read(new File(filename));
      int type = originalImage.getType() == 0? BufferedImage.TYPE_INT_ARGB : originalImage.getType();

      BufferedImage resizeImagePng = resizeImage(originalImage, type);
      ImageIO.write(resizeImagePng, "png", new File(filename));
    } catch(IOException e){
      System.out.println(e.getMessage());
    }
       
  }
 
  private static BufferedImage resizeImage(BufferedImage originalImage, int type){
	
    BufferedImage resizedImage = new BufferedImage(IMG_WIDTH, IMG_HEIGHT, type);
	  Graphics2D g = resizedImage.createGraphics();
	  g.drawImage(originalImage, 0, 0, IMG_WIDTH, IMG_HEIGHT, null);
	  g.dispose();
 
	  return resizedImage;
  }

  public static void main(String[] argv) {
    ImageResize image = new ImageResize("/Users/dclarke/BarFight.png");
  }
}

