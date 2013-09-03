#include <vtkImageData.h>
#include <vtkCellData.h>
#include <vtkPointData.h>
#include <vtkFloatArray.h>
#include <vtkUnsignedCharArray.h>
#include <vtkStructuredPoints.h>
#include <vtkXMLImageDataReader.h>
#include <vtkStructuredPointsReader.h>
#include <vtkImageShiftScale.h>
#include <vtkPNGWriter.h>

#include <limits>
#include <string>
#include <iostream>
using namespace std;

void Write(int dims[3], vtkUnsignedCharArray *colors, const string &outfilebase, const string &outfileext)
{
  vtkImageData *outputData = vtkImageData::New();
  outputData->SetDimensions(dims);
  outputData->GetPointData()->SetScalars(colors);

  string outfile = outfilebase + outfileext;

  vtkPNGWriter *pw = vtkPNGWriter::New();
  pw->SetInputData(outputData);
  pw->SetFileName(outfile.c_str());
  pw->Write();
  pw->Delete();

  outputData->Delete();
}

void EnhanceContrast(float *pScalars, vtkIdType nComps, vtkIdType nTups)
{
  float fmin[4] = {numeric_limits<float>::max()};
  float fmax[4] = {-numeric_limits<float>::max()};
  for (vtkIdType i=0; i<nTups; ++i)
    {
    for (vtkIdType j=0; j<nComps; ++j)
      {
      float val = pScalars[i*nComps+j];
      fmin[j] = fmin[j]>val?val:fmin[j];
      fmax[j] = fmax[j]<val?val:fmax[j];
      }
    }
  for (vtkIdType i=0; i<4; ++i)
    {
    if (fmax[i] == fmin[i])
      {
      fmax[i] = 1.0f;
      fmin[i] = 0.0f;
      }
    else
      {
      fmax[i] = fmax[i] - fmin[i];
      }
    }
  for (vtkIdType i=0; i<nTups; ++i)
    {
    for (vtkIdType j=0; j<nComps; ++j)
      {
      float val = pScalars[i*nComps+j];
       pScalars[i*nComps+j] = (val - fmin[j])/fmax[j];
      }
    }
}

int main(int argc, char *argv[])
{
  vtkStructuredPointsReader *ir = vtkStructuredPointsReader::New();
  vtkXMLImageDataReader *xr = vtkXMLImageDataReader::New();
  vtkUnsignedCharArray *colors = vtkUnsignedCharArray::New();
  colors->SetName("colors");

  int n = argc - 1;
  for (int i=0; i<n; ++i)
    {
    string infile = argv[i+1];

    vtkImageData *data = NULL;
    size_t ext;
    if ((ext = infile.find(".vtk")) != string::npos)
      {
      ir->SetFileName(infile.c_str());
      ir->Update();
      data = static_cast<vtkImageData*>(ir->GetOutput());
      data->Register(0);
      }
    else
    if ((ext = infile.find(".vti")) != string::npos)
      {
      xr->SetFileName(infile.c_str());
      xr->Update();
      data = xr->GetOutput();
      data->Register(0);
      }
    else
      {
      cerr << "Error: Unrecognized infile " << infile << endl;
      continue;
      }
    if (data == NULL)
      {
      cerr << "Error: Failed to read " << infile << endl;
      continue;
      }

    vtkFloatArray *scalars
      = vtkFloatArray::SafeDownCast(data->GetCellData()->GetArray("tex"));
     if (!scalars)
       {
       cerr << "Error: No array named tex" << endl;
       data->Delete();
       continue;
       }

    // for depth and vector textures
    // aply contrast enhancement before
    // conversion
    bool ce
      = (infile.find("depth") != string::npos)
      || (infile.find("vectors") != string::npos);

    string outfilebase = infile.substr(0, ext);

    // convert from cell to point data
    // required by the PNGWriter
    int dims[3];
    data->GetDimensions(dims);
    dims[0] -= 1;
    dims[1] -= 1;

    vtkIdType nComps = scalars->GetNumberOfComponents();
    vtkIdType nTups = scalars->GetNumberOfTuples();
    vtkIdType nVals = nComps*nTups;

    // write RGBA image
    string outfileext = ".png";
    colors->SetNumberOfComponents(nComps);
    colors->SetNumberOfTuples(nTups);
    unsigned char *pColors = colors->GetPointer(0);
    float *pScalars = scalars->GetPointer(0);
    if (ce)
      {
      EnhanceContrast(pScalars, nComps, nTups);
      }
    for (vtkIdType i=0; i<nVals; ++i)
      {
      pColors[i] = static_cast<unsigned char>(255.0f*pScalars[i]);
      }
    Write(dims, colors, outfilebase, outfileext);
    cerr << infile << " -> " << outfilebase + outfileext << endl;

    /*if (nComps<3)
      {
      data->Delete();
      continue;
      }*/

    // write an image for each channel
    colors->SetNumberOfComponents(1);
    colors->SetNumberOfTuples(nTups);
    pColors = colors->GetPointer(0);
    for (vtkIdType j=0; j<nComps; ++j)
      {
      switch (j)
        {
        case 0:
          outfileext = "_R.png";
          break;
        case 1:
          outfileext = "_G.png";
          break;
        case 2:
          outfileext = "_B.png";
          break;
        case 3:
          outfileext = "_A.png";
          break;
        }
      for (vtkIdType i=0; i<nTups; ++i)
        {
        pColors[i] = static_cast<unsigned char>(255.0f*pScalars[i*nComps+j]);
        }
      Write(dims, colors, outfilebase, outfileext);
      cerr << infile << " -> " << outfilebase + outfileext << endl;
      }

    data->Delete();
    }

  ir->Delete();
  xr->Delete();
  colors->Delete();

  return 0;
}
