function [imageName, numImage, imageSize] = getDataStat(dataDir, imageFormat)

% get information of the dataset
% param[in] dataDir: directory of dataset
% param[in] imageFormat: format of images, e.g., jpg, png
% param[out] imageNames: name of images
% param[out] numImage: total number of images under the `dataDir`
% param[out] imageSize: size of each image

if (~exist(dataDir,'dir'))
	imageName = {};
	numImage = NaN;
	imageSize = [NaN, NaN];
    return;
end

imageList = dir([dataDir '/*.' imageFormat]); 
numImage = length(imageList);

imageName = cell(numImage, 1);
imageSize = zeros(numImage, 2);

for i = 1:numImage
	imageName{i} = imageList(i).name;
	im = imread(fullfile(dataDir, imageName{i}));
	imageSize(i,1) = size(im, 1);
	imageSize(i,2) = size(im, 2);
end

end