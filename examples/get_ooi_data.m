function [data] = get_ooi_data(username,token,instrument,t_start,t_end)
%GET_OOI_DATA Retrieves data from the OOI Machine to Machine databse using
%the Your Ocean Data Access Interface Module (YODA_IM). Returns data as a
%JSON object.
%
%   Inputs:
%       username    (string)        Your OOI username
%
%       token       (string)        Your OOI token.
%
%       instrument  (string)        Reference identifier of the OOI
%                                   instrument of interest.
%
%       t_start     (string)        ISO-8601 formated string defining the
%                                   starting time of your data request
%                                   (e.g. 1988-10-29T16:35:00.000Z)
%
%       t_end     (string)        ISO-8601 formated string defining the
%                                 ending time of your data request
%                                   (e.g. 1988-10-29T16:35:00.000Z)
%
%       

    % Assemble URL
    base_url = 'http://35.162.199.89/data/';
    url = [base_url instrument];
    
    % Setup Request Options
    options = weboptions('ContentType','json','Timeout',120);

    % Display Information about the get request
    fprintf('Welcome to YODA_IM - Help you I can, hmmm?\n');
    fprintf('   Retrieving data from: %s\n',base_url);
    fprintf('   Using instrument: %s\n',instrument);
    fprintf('   Over the time period:\n');
    fprintf('      %s to %s\n\n',t_start,t_end);

    % Ask for confirmation and go
    if isempty(input('Read to get data? Press ENTER to confirm, other to quit: ','s'))
        fprintf('\n\n... and awaaaaaayyy we go!\n\n');
        data = webread(url,'username',username,'token',token,'begin_date',t_start,'end_date',t_end,options);
        if ~isempty(data)
            fprintf('\n\n NAILED IT! \n\n');
        else
            warning('Something went wrong :(  (didnt nail it)');
        end
    else
        fprintf('\n\nOkay, cool. Peace yo[da]\n\n');
    end
    
end

