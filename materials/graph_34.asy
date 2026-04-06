size(200);

// Draw the square PQRS
pair P = (0, 1);
pair Q = (0, 0);
pair R = (1, 0);
pair S = (1, 1);

draw(P--Q--R--S--cycle);

// Point T is on line QR extended
pair T = (1.5, 0);
draw(R--T);

// Point U is on line RS
pair U = (1, 0.2); // Just an approximation based on the drawing
draw(S--U);

// Draw diagonal PR
draw(P--R);

// Draw lines PUT and QRT (QRT is just Q--R--T which is already drawn)
draw(P--U--T);

// Add labels
label("$P$", P, NW);
label("$Q$", Q, SW);
label("$R$", R, SE);
label("$S$", S, NE);
label("$T$", T, E);
label("$U$", U, NE);

// Mark right angles for square corners (only Q and R are marked in the image)
import markers;
markangle(radius=10, P, Q, R);
markangle(radius=10, Q, R, S); // Actually marked inside the square at R
markangle(radius=10, R, S, P);

// Note lengths (optional, based on image annotations)
// RT = 2.1 cm
// TU = 2.9 cm
label("2.1", (R+T)/2, S);
label("2.9", (U+T)/2, NE);
