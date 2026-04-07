size(800, 800);
defaultpen(linewidth(0.8));
pair P = (0, 42);
pair Q = (0, 0);
pair R = (42, 0);
pair S = (42, 42);
pair T = (44.1, 0);
pair U = (42, 2);
draw(P--Q);
draw(Q--R);
draw(R--S);
draw(S--P);
draw(R--T);
draw(P--T);
label("$P$", P, NW);
label("$Q$", Q, SW);
label("$R$", R, SW);
label("$S$", S, NE);
label("$T$", T, E);
label("$U$", U, NE);
{
    pair vec1 = unit(P - Q);
    pair vec2 = unit(R - Q);
    pair pt1 = Q + 1.0*vec1;
    pair pt2 = Q + 1.0*vec2;
    pair corner = Q + 1.0*vec1 + 1.0*vec2;
    draw(pt1--corner--pt2);
}
{
    pair vec1 = unit(Q - R);
    pair vec2 = unit(S - R);
    pair pt1 = R + 1.0*vec1;
    pair pt2 = R + 1.0*vec2;
    pair corner = R + 1.0*vec1 + 1.0*vec2;
    draw(pt1--corner--pt2);
}
{
    pair mid = (R + T) / 2.0;
    label("2.1", mid, S);
}
{
    pair mid = (U + T) / 2.0;
    label("2.9", mid, NE);
}