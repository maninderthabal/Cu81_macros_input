{
//before running this macro, load the NuTOFSpec.cxx first by running
//.L NuTOFSpec.cxx+
//in a new root session
TotalNuTOFSpec h1("h1", true);

//create an object h1
h1.SetFile("Ga83_sumw2.root");
//h1.SetFile("Ga83_1348keV_hagrid.root");
// h2.SetFile("Ga83_gamma_gated.root");
//Load the root file containing experimental 1d or 2d histograms
//Replace the root file to yours.

h1.SetNuEffPar(0, 1, 1);
// h1.SetPn(0.56, 0.07);    //Pn value of decay
h1.SetPn(0.75, 0.223);

//h1.SetHalfLife(308, 10); // Ga83 half-life
h1.SetHalfLife(68.5, 6.4); // Cu81 half-life

h1.SetFixLineColor(4);
h1.SetFitLineColor(4);
h1.SetFitResultColor(6);
h1.SetGeScaleFactor(0.75, 0.7);

h1.SetRespFuncType(1);
//Set which response function to use. Change the number "1" to match whatever value you
//want to use in TotalNuMonState::CalFunc(double *xx, double *par) (you need to look into
//this function in NuTOFSpec.cxx and modify it accordingly

h1.SetNumOfBinsPerNS_NeutronSingle(1.0); // neutron singles
                                         // h1.SetNumOfBinsPerNS_NeutronGamma(2.0);  //orginial binning

h1.FitGammaFlashPeak(0, 0, -1, "", 4, -5, 15);

h1.SetTOFLength(106.5, 0.5);
//give the TOF length (and uncertainty). In my example 105+-0.5 cm
h1.DetermineTOFOffset();
//This is to calculate your TOF offset (in ns) based on the gamma-flash centroid
//fitted above
h1.SetIfExpBkg(0);

h1.SetFile("Cu81_singles.root");


//h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_10200_003.input");
//h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_9200_003.input");
//h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_8055_808.input");
//h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_5551_85.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_4744_02.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_4371_749.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_3947_231.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_3719_847.input");
//h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_3484_565.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_3247_084.input");
h1.AddNuPeak("input/Cu81_Zn81.input", "input/Zn81_3064_584.input");







// h1.FitGammaFlashTail(bkg, 1, "RVL", 10, 35);

h1.SetCommonAddSigma(4.0);

for (int n = 0; n < h1.NumOfPeaks; n++)
{
    h1.SetAddSigma(n, 0);
}
// //
h1.PlotExpSpec(0, 600, 0, 30000, "", 3, -1, -100, -100, 4);

double bkg = h1.CalConstBkg(300, 600);



//h1.FitGammaFlashTail(bkg, 1, "RVL", 20, 35);

h1.PlotSimSpec(bkg, "same", 1.0);

h1.FitHist(30, 600, 0, "RVM");
h1.Hist->Draw("hist");
h1.Hist->SetFillColor(kGreen);
h1.PlotSimSpec(bkg, "same", 1.0);
h1.CalBranchingRatio(); // This needs neutron-efficiency curve for accurate determination.
h1.CalLogFT();
h1.PrintFitResult();
h1.PlotResidual(30, 600);


// ////Plot the total response function (with scale 1) with the given bkg computed
}
