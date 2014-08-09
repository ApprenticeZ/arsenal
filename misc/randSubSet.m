% randomly choose subset from `inDir`
% save the selected subset in `outDir`
%
% param[in] inDir: directory of the original whole dataset
% param[in] outDir: directory to save the selected subset
% param[in] subsetSize: the size of subset

function randSubSet(inDir, outDir, subsetSize, imageFormat)
	[imageName, numImage, ~] = getDataStat(inDir, imageFormat);
	if(subsetSize > numImage)
		disp('subset size must be smaller than the original dataset size');
		return;
	end

	selInd = randperm(numImage, subsetSize);
	for i=1:subsetSize
		copyfile(fullfile(inDir,imageName{selInd(i)}),fullfile(outDir,imageName{selInd(i)}));
	end
	filename = imageName{selInd};
	save(fullfile(outDir,'SubsetConfig.mat'), 'selInd', 'filename');
end