package main

import (
    "io/ioutil"

    "github.com/pulumi/pulumi-aws/sdk/v3/go/aws/s3"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create an AWS resource (S3 Bucket)
        bucket, err := s3.NewBucket(ctx, "pulumi-go-01", &s3.BucketArgs{
            // Acl: pulumi.String("private"),
            // Tags: {
            //     { "Environment", "Dev" },
            //     { "Name", "pulumi-dotnet-01" },
            // },
            Website: s3.BucketWebsiteArgs{
                IndexDocument: pulumi.String("index.html"),
            },
        })
        // Export the name of the bucket
        ctx.Export("bucketName", bucket.ID())
        ctx.Export("bucketEndpoint", pulumi.Sprintf("http://%s", bucket.WebsiteEndpoint))

        htmlContent, err := ioutil.ReadFile("site/index.html")
        if err != nil {
            return err
        }

        _, err = s3.NewBucketObject(ctx, "index.html", &s3.BucketObjectArgs{
            Bucket:  bucket.ID(),
            Content: pulumi.String(string(htmlContent)),
            Acl:         pulumi.String("public-read"),
            ContentType: pulumi.String("text/html"),
        })
        if err != nil {
            return err
        }


        return nil
    })
}
