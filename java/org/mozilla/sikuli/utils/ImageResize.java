/*
 * Package: org.mozilla.sikuli.utils
 * 
 * File: ImageResize.java
 * 
 * Date: 1/17/2012
 */

package org.mozilla.sikuli.utils;

import java.awt.Graphics2D;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/**
 * Helper library to resize an image for a particular filename based on the type
 * specified.
 * 
 * @author David Clarke
 */
public class ImageResize {

	/**
	 * The width to resize the image to
	 */
	private static final int IMG_WIDTH = 70;

	/**
	 * The height to resize the image to
	 */
	private static final int IMG_HEIGHT = 63;

	/**
	 * Constructs an ImageResize object for a specified filename.
	 * 
	 * @param filename the image file to read and resize
	 */
	public ImageResize(String filename) {
		try {
			BufferedImage originalImage = ImageIO.read(new File(filename));
			int type = originalImage.getType() == 0 ? BufferedImage.TYPE_INT_ARGB
					: originalImage.getType();

			BufferedImage resizeImagePng = resizeImage(originalImage, type);
			ImageIO.write(resizeImagePng, "png", new File(filename));
		} catch (IOException e) {
			System.out.println(e.getMessage());
		}

	}

	/**
	 * Resizes the image speciifed to the type specified with the constant width
	 * and height.
	 * 
	 * @param originalImage the original image to be resized
	 * @param type the type of the existing image
	 * 
	 * @return the resized image
	 */
	private static BufferedImage resizeImage(BufferedImage originalImage,
			int type) {

		BufferedImage resizedImage = new BufferedImage(IMG_WIDTH, IMG_HEIGHT,
				type);
		Graphics2D g = resizedImage.createGraphics();
		g.drawImage(originalImage, 0, 0, IMG_WIDTH, IMG_HEIGHT, null);
		g.dispose();

		return resizedImage;
	}

	/**
	 * Test method to verify that the image specified on the command line can be
	 * resized.
	 * 
	 * @param argv[0] the file location of the image to resize
	 */
	public static void main(String[] argv) {
		if (argv.length == 1) {
			ImageResize image = new ImageResize(argv[0]);
		} else {
			System.err.println("Usage: java ImageResize filename");
		}
	}

} // ImageResize
