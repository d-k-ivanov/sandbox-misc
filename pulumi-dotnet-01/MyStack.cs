using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Aws.S3.Inputs;

using System.IO;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an AWS resource (S3 Bucket)
        var bucket = new Bucket("pulumi-dotnet-01", new BucketArgs
        {
            // Acl = "private",
            Tags =
            {
                { "Environment", "Dev" },
                { "Name", "pulumi-dotnet-01" },
            },
            Website = new BucketWebsiteArgs
            {
                IndexDocument = "index.html"
            },
        });

        // Export the name of the bucket
        this.BucketName = bucket.Id;
        this.BucketEndpoint = Output.Format($"http://{bucket.WebsiteEndpoint}");

        var filePath        = Path.GetFullPath("./site/index.html");
        var hmtlString      = File.ReadAllText(filePath);
        var bucketObject    = new BucketObject("index.html", new BucketObjectArgs
        {
            Bucket = bucket.BucketName,
            Content = hmtlString,
            Acl = "public-read",
            ContentType = "text/html",
        });
    }

    [Output] public Output<string> BucketName       { get; set; }
    [Output] public Output<string> BucketEndpoint   { get; set; }
}
