% Load vehicle data set
data = load('fasterRCNNVehicleTrainingData.mat');
vehicleDataset = data.vehicleTrainingData;
% Display first few rows of the data set.
vehicleDataset(1:4,:)
% Add fullpath to the local vehicle data folder.
dataDir = fullfile(toolboxdir('vision'),'visiondata');
vehicleDataset.imageFilename = fullfile(dataDir, vehicleDataset.imageFilename);
% Read one of the images.
I = imread(vehicleDataset.imageFilename{10});
% Insert the ROI labels.
I = insertShape(I, 'Rectangle', vehicleDataset.vehicle{10});
% Resize and display image.
I = imresize(I,3);
figure
imshow(I)